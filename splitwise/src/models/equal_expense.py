from src.models.user import User
from src.models.expense import Expense
from src.models.split import Split
from src.models.equal_split import EqualSplit
from src.models.expense_metadata import ExpenseMetadata


class EqualExpense(Expense):
    def __init__(
        self,
        amount: float,
        paid_by: User,
        splits: list[Split],
        metadata: ExpenseMetadata,
    ) -> None:
        super().__init__(amount, paid_by, splits, metadata)

    def validate(self) -> bool:
        return all(isinstance(split, EqualSplit) for split in self.splits)
