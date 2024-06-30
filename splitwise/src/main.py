from src.models.split import Split
from src.services.expense_manager import ExpenseManager
from src.models.user import User
from src.models.expense_type import ExpenseType
from src.models.equal_split import EqualSplit
from src.models.exact_split import ExactSplit
from src.models.percent_split import PercentSplit

expenseManager = ExpenseManager()

expenseManager.add_user(User("u1", "User1", "gaurav@workat.tech", "9876543210"))
expenseManager.add_user(User("u2", "User2", "sagar@workat.tech", "9876543210"))
expenseManager.add_user(User("u3", "User3", "hi@workat.tech", "9876543210"))
expenseManager.add_user(
    User("u4", "User4", "mock-interviews@workat.tech", "9876543210")
)

while True:
    command = input()
    commands = command.split(" ")
    command_type = commands[0]

    if command_type == "SHOW":
        if len(commands) == 1:
            expenseManager.show_balances()
        else:
            expenseManager.show_balance(commands[1])
    elif command_type == "EXPENSE":
        paid_by = commands[1]
        amount = float(commands[2])
        no_of_users = int(commands[3])
        expense_type = commands[4 + no_of_users]
        splits = []
        if expense_type == "EQUAL":
            for i in range(no_of_users):
                splits.append(EqualSplit(expenseManager.user_map[commands[4 + i]]))
            expenseManager.add_expense(ExpenseType.EQUAL, amount, paid_by, splits, None)
        elif expense_type == "EXACT":
            for i in range(no_of_users):
                splits.append(
                    ExactSplit(
                        expenseManager.user_map[commands[4 + i]],
                        float(commands[5 + no_of_users + i]),
                    )
                )
            expenseManager.add_expense(ExpenseType.EXACT, amount, paid_by, splits, None)
        elif expense_type == "PERCENT":
            for i in range(no_of_users):
                splits.append(
                    PercentSplit(
                        expenseManager.user_map[commands[4 + i]],
                        float(commands[5 + no_of_users + i]),
                    )
                )
            expenseManager.add_expense(
                ExpenseType.PERCENT, amount, paid_by, splits, None
            )
    elif command_type == "EXIT":
        print("Exiting...")
        break
