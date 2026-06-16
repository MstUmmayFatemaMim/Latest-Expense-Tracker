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
    def _show_and_select(cls, user_id, action):
        all_data = AllConnection.read_data(AllConnection.Expense_File_Path)
        serial_map = {}

        print(f"\n--- Select Expense to {action} ---")
        serial = 1
        for i, row in enumerate(all_data):
            if row.get("user_id") == user_id and row.get("total_price"):
                serial_map[serial] = i
                print(f"{serial}. {row['date']} | {row['product']} | {row['total_price']}")
                serial += 1

        if serial == 1:
            print("No expenses found!")
            return None, None, None

        choice = int(input("\nEnter number: "))
        return all_data, choice, serial_map

    @classmethod
    def edit_expense(cls, user_id):
        all_data, choice, serial_map = cls._show_and_select(user_id, "Edit")
        if all_data is None:
            return

        index = serial_map[choice]
        row = all_data[index]

        row['product'] = input("New product: ") or row['product']
        row['quantity'] = input("New quantity: ") or row['quantity']
        row['price'] = input("New price: ") or row['price']
        row['total_price'] = float(row['quantity']) * float(row['price'])
        row['date'] = AllConnection.get_manual_date()

        open(AllConnection.Expense_File_Path, "w").close()
        for row in all_data:
            AllConnection.write_and_save_data(
                AllConnection.Expense_File_Path,
                AllConnection.Expense_Column, row)
        print("Updated successfully!")

    @classmethod
    def delete_expense(cls, user_id):
        all_data, choice, serial_map = cls._show_and_select(user_id, "Delete")
        if all_data is None:
            return

        index = serial_map[choice]
        all_data.pop(index)

        open(AllConnection.Expense_File_Path, "w").close()
        for row in all_data:
            AllConnection.write_and_save_data(
                AllConnection.Expense_File_Path,
                AllConnection.Expense_Column, row)
        print("Deleted successfully!")

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
