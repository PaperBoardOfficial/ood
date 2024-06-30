from src.models.user import User
from src.models.split import Split
from src.models.expense_metadata import ExpenseMetadata


class Expense:
    def __init__(
        self,
        amount: float,
        paid_by: User,
        splits: list[Split],
        metadata: ExpenseMetadata,
    ) -> None:
        self.id: str = ""
        self.amount: float = amount
        self.paid_by: User = paid_by
        self.splits: list[Split] = splits
        self.metadata: ExpenseMetadata = metadata

    def get_id(self) -> str:
        return self.id

    def set_id(self, id: str) -> None:
        self.id = id

    def get_amount(self) -> float:
        return self.amount

    def set_amount(self, amount: float) -> None:
        self.amount = amount

    def get_paid_by(self) -> User:
        return self.paid_by

    def set_paid_by(self, paid_by: User) -> None:
        self.paid_by = paid_by

    def get_splits(self) -> list[Split]:
        return self.splits

    def set_splits(self, splits: list[Split]) -> None:
        self.splits = splits

    def get_metadata(self) -> ExpenseMetadata:
        return self.metadata

    def set_metadata(self, metadata: ExpenseMetadata) -> None:
        self.metadata = metadata

    def validate(self) -> bool:
        raise NotImplementedError("Subclass must implement abstract method")
