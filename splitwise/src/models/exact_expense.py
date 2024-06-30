from src.models.user import User
from src.models.expense import Expense
from src.models.split import Split
from src.models.exact_split import ExactSplit
from src.models.expense_metadata import ExpenseMetadata

class ExactExpense(Expense):
    def __init__(self, amount: float, paid_by: User, splits: list[Split], metadata: ExpenseMetadata) -> None:
        super().__init__(amount, paid_by, splits, metadata)

    def validate(self) -> bool:
        if not all(isinstance(split, ExactSplit) for split in self.splits):
            return False

        total_amount = self.amount
        sum_split_amount = sum(split.amount for split in self.splits if isinstance(split, ExactSplit))

        return total_amount == sum_split_amount