from src.models.user import User
from src.models.expense import Expense
from src.models.percent_split import PercentSplit
from src.models.expense_metadata import ExpenseMetadata
from src.models.split import Split

class PercentExpense(Expense):
    def __init__(self, amount: float, paid_by: User, splits: list[Split], metadata: ExpenseMetadata) -> None:
        super().__init__(amount, paid_by, splits, metadata)

    def validate(self) -> bool:
        if not all(isinstance(split, PercentSplit) for split in self.splits):
            return False

        total_percent = 100
        sum_split_percent = sum(split.percent for split in self.splits if isinstance(split, PercentSplit))

        return total_percent == sum_split_percent