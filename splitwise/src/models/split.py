from src.models.user import User

class Split:
    def __init__(self, user: User) -> None:
        self.user: User = user
        self.amount: float = 0.0

    def get_user(self) -> User:
        return self.user

    def set_user(self, user: User) -> None:
        self.user = user

    def get_amount(self) -> float:
        return self.amount

    def set_amount(self, amount: float) -> None:
        self.amount = amount