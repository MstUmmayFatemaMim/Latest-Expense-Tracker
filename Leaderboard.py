import csv
from Config import AllConnection


class LeaderBoard:

    def get_user_map(self):
        user_map = {}
        user_rows = AllConnection.read_data(AllConnection.User_File_Path)
        for row in user_rows:
            user_map[row["user_id"]] = row["user_name"]
        return user_map

    def display_ranking(self, title, user_data):
        ranking_list = []
        for name, total in user_data.items():
            ranking_list.append([total, name])

        ranking_list.sort(reverse=True)

        print(f"\nRank  Username       {title}")
        print("-" * 33)
        rank = 1
        for total, name in ranking_list[:3]:
            print(f"{rank:<5} {name:<14} {total}")
            rank = rank + 1

    def view_by_income(self):
        user_map = self.get_user_map()
        user_incomes = {}

        expense_rows = AllConnection.read_data(AllConnection.Expense_File_Path)
        for row in expense_rows:
            if row["user_id"] != "" and row["income"] != "":
                name = user_map.get(row["user_id"], "Unknown")
                amount = float(row["income"])

                if name in user_incomes:
                    user_incomes[name] = user_incomes[name] + amount
                else:
                    user_incomes[name] = amount

        self.display_ranking("Total Income", user_incomes)

    def view_by_expense(self):
        user_map = self.get_user_map()
        user_expenses = {}

        expense_rows = AllConnection.read_data(AllConnection.Expense_File_Path)
        for row in expense_rows:
            if row["user_id"] != "" and row["total_price"] != "" and row["income"] == "":
                name = user_map.get(row["user_id"], "Unknown")
                amount = float(row["total_price"])

                if name in user_expenses:
                    user_expenses[name] = user_expenses[name] + amount
                else:
                    user_expenses[name] = amount

        self.display_ranking("Total Expense", user_expenses)

    def view_by_balance(self):
        user_map = self.get_user_map()
        user_balances = {}

        expense_rows = AllConnection.read_data(AllConnection.Expense_File_Path)
        for row in expense_rows:
            if row["user_id"] != "":
                name = user_map.get(row["user_id"], "Unknown")

                if name not in user_balances:
                    user_balances[name] = 0.0

                if row["income"] != "":
                    user_balances[name] = user_balances[name] + float(row["income"])
                if row["total_price"] != "" and row["income"] == "":
                    user_balances[name] = user_balances[name] - float(row["total_price"])

        self.display_ranking("Total Balance", user_balances)

    def show_leaderboard(self):
        while True:
            print("\n===== LEADERBOARD =====")
            print("1. View by Income")
            print("2. View by Expense")
            print("3. View by Balance")
            print("4. Go Back")

            choice = input("\nChoose: ").strip()

            if choice == "1":
                self.view_by_income()
            elif choice == "2":
                self.view_by_expense()
            elif choice == "3":
                self.view_by_balance()
            elif choice == "4":
                print("Going back.");
                break
            else:
                print("Invalid choice.")
