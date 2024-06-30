from src.models.user import User
from src.models.expense import Expense
from src.models.expense_metadata import ExpenseMetadata
from src.models.split import Split
from src.models.exact_expense import ExactExpense
from src.models.percent_expense import PercentExpense
from src.models.equal_expense import EqualExpense
from src.models.expense_type import ExpenseType
from src.models.percent_split import PercentSplit


class ExpenseService:
    @staticmethod
    def create_expense(
        expense_type: ExpenseType,
        amount: float,
        paid_by: User,
        splits: list[Split],
        expense_metadata: ExpenseMetadata,
    ) -> Expense | None:
        if expense_type == ExpenseType.EXACT:
            return ExactExpense(amount, paid_by, splits, expense_metadata)
        elif expense_type == ExpenseType.PERCENT:
            for split in splits:
                split.amount = (amount * split.percent) / 100.0
            return PercentExpense(amount, paid_by, splits, expense_metadata)
        elif expense_type == ExpenseType.EQUAL:
            total_splits = len(splits)
            split_amount = round(amount * 100 / total_splits) / 100.0
            for split in splits:
                split.amount = split_amount
            splits[0].amount += amount - split_amount * total_splits
            return EqualExpense(amount, paid_by, splits, expense_metadata)
        else:
            return None
