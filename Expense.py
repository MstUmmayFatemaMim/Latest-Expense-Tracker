from ftplib import all_errors

from Config import AllConnection


class Expense:
    def __init__(self, user_id, category, product, quantity, price):
        self.user_id = user_id
        self.category = category
        self.product = product
        self.quantity = float(quantity)
        self.price = float(price)
        self.total_price = self.price * self.quantity
        self.date = AllConnection.get_manual_date()

        AllConnection.write_and_save_data(
            AllConnection.Expense_File_Path,
            AllConnection.Expense_Column,
            {
                "user_id": self.user_id,
                "category": self.category,
                "product": self.product,
                "quantity": self.quantity,
                "price": self.price,
                "total_price": self.total_price,
                "date": self.date,
            }
        )
        print(f"{self.category} Expense added successfully on {self.date}")

    @classmethod
    def add_food_expense(cls,
                         user_id):  ### Like to inherit.It is subclass(add_food_expense) when I call from here,all method come to subclass
        product = input("Enter the food name: ")
        quantity = input("Enter the quantity: ")
        price = input("Enter the price: ")
        cls(user_id, "Food", product, quantity, price)

    @classmethod
    def add_shopping_expense(cls, user_id):
        product = input("Enter the shopping item: ")
        quantity = input("Enter the quantity: ")
        price = input("Enter the price: ")
        cls(user_id, "Shopping", product, quantity, price)

    @classmethod
    def add_health_expense(cls, user_id):
        product = input("Enter the health item: ")
        quantity = input("Enter the quantity: ")
        price = input("Enter the price: ")
        cls(user_id, "Health", product, quantity, price)

    @classmethod
    def show_selected_expense(cls, user_id):
        all_data = AllConnection.read_data(AllConnection.Expense_File_Path)
        user_expense = []
        index = 0
        for row in all_data:
            if row["user_id"] == user_id and row["income"] == "":
                user_expense.append(row)
                print(f"{index}. {row['product']}    {row['total_price']}   {row['date']}")
                index = index + 1

        choice = int(input("Select the index number: "))
        selected_row = user_expense[choice]
        return selected_row, all_data

    @classmethod
    def edit_expense(cls, user_id):
        selected_row, all_data = cls.show_selected_expense(user_id)
        new_product = input("Enter the new product name: ")
        new_quantity = input("Enter the new quantity: ")
        new_price = input("Enter the new price: ")

        if new_product != "":
            selected_row["product"] = new_product
        if new_quantity != "":
            selected_row["quantity"] = new_quantity
        if new_price != "":
            selected_row["price"] = new_price

        selected_row["total_price"] = float(selected_row["price"]) * float(selected_row["quantity"])
        selected_row["date"] = AllConnection.get_manual_date()

        open(AllConnection.Expense_File_Path, "w", encoding="utf-8").close()

        for row in all_data:
            AllConnection.write_and_save_data(AllConnection.Expense_File_Path, AllConnection.Expense_Column, row)
        print("Updated successfully")

    @classmethod
    def delete_expense(cls, user_id):
        selected_row, all_data = cls.show_selected_expense(user_id)
        open(AllConnection.Expense_File_Path, "w", encoding="utf-8").close()
        for row in all_data:
            if row != selected_row:
                AllConnection.write_and_save_data(AllConnection.Expense_File_Path, AllConnection.Expense_Column, row)
        print("Deleted successfully")

    @classmethod
    def expense(cls, user_id):
        while True:
            print(f"\n===== Choose Your Expense Category =====")
            print(f"1. Food")
            print(f"2. Shopping")
            print(f"3. Health")
            print(f"4. Edit Expense")
            print(f"5. Delete Expense")
            print(f"6.Back")
            choice = input("\nChoose: ").strip()
            if choice == "1":
                Expense.add_food_expense(user_id)
            elif choice == "2":
                Expense.add_shopping_expense(user_id)
            elif choice == "3":
                Expense.add_health_expense(user_id)
            elif choice == "4":
                Expense.edit_expense(user_id)
            elif choice == "5":
                Expense.delete_expense(user_id)
            elif choice == "6":
                print("Going back to Dashboard!")
                break
            else:
                print("Invalid Choice")
