from src.models.user import User
from src.models.split import Split

class ExactSplit(Split):
    def __init__(self, user: User, amount: float) -> None:
        super().__init__(user)
        self.amount: float = amount