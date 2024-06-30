from src.models.user import User
from src.models.expense import Expense
from src.models.expense_metadata import ExpenseMetadata
from src.models.expense_type import ExpenseType
from src.models.split import Split
from src.services.expense_service import ExpenseService


class ExpenseManager:
    def __init__(self) -> None:
        self.expenses: list[Expense] = []
        self.user_map: dict[str, User] = {}
        self.balance_sheet: dict[str, dict[str, float]] = {}

    def add_user(self, user: User) -> None:
        self.user_map[user.get_id()] = user
        self.balance_sheet[user.get_id()] = {}

    def add_expense(
        self,
        expense_type: ExpenseType,
        amount: float,
        paid_by: str,
        splits: list[Split],
        expense_metadata: ExpenseMetadata,
    ) -> None:
        expense = ExpenseService.create_expense(
            expense_type, amount, self.user_map[paid_by], splits, expense_metadata
        )
        self.expenses.append(expense)
        for split in expense.get_splits():
            paid_to = split.get_user().get_id()
            balances = self.balance_sheet.get(paid_by, {})
            balances[paid_to] = balances.get(paid_to, 0.0) + split.get_amount()

            balances = self.balance_sheet.get(paid_to, {})
            balances[paid_by] = balances.get(paid_by, 0.0) - split.get_amount()

    def show_balance(self, user_id: str) -> None:
        is_empty = True
        for user, amount in self.balance_sheet[user_id].items():
            if amount != 0:
                is_empty = False
                self.print_balance(user_id, user, amount)

        if is_empty:
            print("No balances")

    def show_balances(self) -> None:
        is_empty = True
        for user, balances in self.balance_sheet.items():
            for other_user, amount in balances.items():
                if amount > 0:
                    is_empty = False
                    self.print_balance(user, other_user, amount)

        if is_empty:
            print("No balances")

    def print_balance(self, user1: str, user2: str, amount: float) -> None:
        user1_name = self.user_map[user1].get_name()
        user2_name = self.user_map[user2].get_name()
        if amount < 0:
            print(f"{user1_name} owes {user2_name}: {abs(amount)}")
        elif amount > 0:
            print(f"{user2_name} owes {user1_name}: {abs(amount)}")
