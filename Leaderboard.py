from Config import AllConnection


class LeaderBoard:

    def process_and_print_leaderboard(self, user_amounts, title):
        all_users = AllConnection.read_data(AllConnection.User_File_Path)
        id_to_name_map = {}
        for user in all_users:
            id_to_name_map[user["user_id"]] = user["user_name"]

        ranking_list = []
        for user_id, total in user_amounts.items():
            actual_name = id_to_name_map.get(user_id, user_id)
            ranking_list.append([total, actual_name])

        ranking_list.sort(reverse=True)

        print(f"\nRank  Username       Total {title}")
        print("-" * 35)
        rank = 1
        for total, name in ranking_list[:3]:
            print(f"{rank:<5} {name:<14} {total:.2f}")
            rank = rank + 1

    def view_by_income(self):
        user_incomes = {}
        all_data = AllConnection.read_data(AllConnection.Expense_File_Path)

        for row in all_data:
            if row.get("user_id") and row.get("income"):
                name = row["user_id"]
                amount = float(row["income"])

                if name in user_incomes:
                    user_incomes[name] = user_incomes[name] + amount
                else:
                    user_incomes[name] = amount

        self.process_and_print_leaderboard(user_incomes, "Income")

    def view_by_expense(self):
        user_expenses = {}
        all_data = AllConnection.read_data(AllConnection.Expense_File_Path)

        for row in all_data:
            if row.get("user_id") and row.get("total_price"):
                name = row["user_id"]
                amount = float(row["total_price"])

                if name in user_expenses:
                    user_expenses[name] = user_expenses[name] + amount
                else:
                    user_expenses[name] = amount

        self.process_and_print_leaderboard(user_expenses, "Expense")

    def view_by_balance(self):
        user_balances = {}
        all_data = AllConnection.read_data(AllConnection.Expense_File_Path)

        for row in all_data:
            if row.get("user_id"):
                name = row["user_id"]

                if name not in user_balances:
                    user_balances[name] = 0.0

                if row.get("income"):
                    user_balances[name] = user_balances[name] + float(row["income"])
                if row.get("total_price"):
                    user_balances[name] = user_balances[name] - float(row["total_price"])

        self.process_and_print_leaderboard(user_balances, "Balance")

    def view_by_category(self):
        user_categories = {}
        cat = input("Enter category to compare (Food/Shopping/Health): ").strip()
        all_data = AllConnection.read_data(AllConnection.Expense_File_Path)

        for row in all_data:
            if row.get("user_id") and row.get("category") == cat and row.get("total_price"):
                name = row["user_id"]
                amount = float(row["total_price"])

                if name in user_categories:
                    user_categories[name] = user_categories[name] + amount
                else:
                    user_categories[name] = amount

        self.process_and_print_leaderboard(user_categories, f"Expense ({cat})")

    def show_leaderboard(self):
        while True:
            print(f"\n===== LEADERBOARD =====")
            print("1. View by Income")
            print("2. View by Expense")
            print("3. View by Balance")
            print("4. View by Category")
            print("5. Show all ranking")
            print("6. Go Back")

            choice = input("\nChoose: ").strip()

            if choice == "1":
                self.view_by_income()
            elif choice == "2":
                self.view_by_expense()
            elif choice == "3":
                self.view_by_balance()
            elif choice == "4":
                self.view_by_category()
            elif choice == "5":
                print("\n===================     GENERATING ALL LEADERBOARDS    ===================")
                self.view_by_income()
                self.view_by_expense()
                self.view_by_balance()
            elif choice == "6":
                print("Going back.")
                break
            else:
                print("Invalid choice.")
