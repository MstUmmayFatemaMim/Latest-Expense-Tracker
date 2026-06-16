from Config import AllConnection
from Expense import Expense
from Leaderboard import LeaderBoard


class DashBoard:
    def __init__(self, user_data):
        self.user_id = user_data["user_id"]
        self.user_name = user_data["user_name"]

    def add_income(self):
        income_amount = input("Enter income amount: ")
        transaction_date = AllConnection.get_manual_date()
        income_data = {
            "user_id": self.user_id,
            "income": income_amount,
            "date": transaction_date,
        }
        AllConnection.write_and_save_data(AllConnection.Expense_File_Path, AllConnection.Expense_Column, income_data)
        print(f"Income added successfully  {transaction_date}")

    def _get_data(self, start=None, end=None):
        all_data = AllConnection.read_data(AllConnection.Expense_File_Path)
        total_income = 0
        total_expense = 0
        purchases = []

        for row in all_data:
            if row["user_id"] == self.user_id:
                if start and end:
                    row_month = row["date"][:7]
                    if not start <= row_month <= end:
                        continue
                if row.get("income"):
                    total_income += float(row["income"])
                if row.get("total_price"):
                    total_expense += float(row["total_price"])
                    purchases.append(row)

        output = f"\n======= Report ({start} to {end}) =======\n"
        output += f"  Income  : {total_income:.2f}\n"
        output += f"  Expense : {total_expense:.2f}\n"
        output += f"  Balance : {total_income - total_expense:.2f}\n"
        output += f"\n------- Purchase Details -------\n"
        for row in purchases:
            output += f"  {row['date']} | {row['category']:10} | {row['product']:15} | {row['total_price']}\n"

        print(output)
        return output

    def view_balance(self):
        self._get_data()

    def view_single_month(self):
        month = input("Enter month (YYYY-MM): ").strip()
        self._get_data(month, month)

    def view_monthly_range(self):
        start = input("Enter start (YYYY-MM): ").strip()
        end = input("Enter end   (YYYY-MM): ").strip()
        if start > end:
            start, end = end, start
        self._get_data(start, end)

    def export(self):
        output = self._get_data()
        with open(f"{self.user_name}_report.txt", "w", encoding="utf-8") as f:
            f.write(output)
        print(f"Saved as {self.user_name}_report.txt")

    def view_monthly(self):
        print("\n1. Single Month")
        print("2. Month Range")
        choice = input("Choose: ").strip()
        if choice == "1":
            self.view_single_month()
        elif choice == "2":
            self.view_monthly_range()
        else:
            print("Invalid Choice")

    def dashboard(self):
        while True:
            print(f"\n===== Dashboard ({self.user_name}) =====")
            print("1. Add Income")
            print("2. Expense")
            print("3. View Balance")
            print("4. Leaderboard")
            print("7. Export File")
            print("8. Monthly Budget")
            print("9. Logout")

            choice = input("\nChoose: ").strip()

            if choice == "1":
                self.add_income()
            elif choice == "2":
                Expense.expense(self.user_id)
            elif choice == "3":
                self.view_balance()
            elif choice == "4":
                LeaderBoard().show_leaderboard()
            elif choice == "7":
                self.export()
            elif choice == "8":
                self.view_monthly()
            elif choice == "9":
                print("Going back.")
                break  #########   It jumps only one level.
            else:
                print("Invalid choice.")
