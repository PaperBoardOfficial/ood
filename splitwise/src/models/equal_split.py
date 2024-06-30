from src.models.user import User
from src.models.split import Split

class EqualSplit(Split):
    def __init__(self, user: User) -> None:
        super().__init__(user)