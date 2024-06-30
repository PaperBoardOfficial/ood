from src.models.user import User
from src.models.split import Split

class PercentSplit(Split):
    def __init__(self, user: User, percent: float) -> None:
        super().__init__(user)
        self.percent: float = percent

    def get_percent(self) -> float:
        return self.percent

    def set_percent(self, percent: float) -> None:
        self.percent = percent