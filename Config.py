import csv
import os
from datetime import date


class AllConnection:
    User_File_Path = r"UserTracker.csv"
    User_Column = ["user_name", "password", "user_id"]
    Expense_File_Path = r"ExpenseTracker.csv"
    Expense_Column = ["user_id", "income", "category", "product", "quantity", "price", "total_price", "date"]

    @classmethod
    def read_data(cls, file_path):
        rows = []
        if not os.path.exists(file_path):
            return rows
        with open(file_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
        return rows

    @classmethod
    def write_and_save_data(cls, file_path, columns, data_dict):
        file_exists = os.path.exists(file_path) and os.path.getsize(file_path) > 0  # ✅ শুধু এই line
        with open(file_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore", restval="")
            if not file_exists:
                writer.writeheader()
            writer.writerow(data_dict)

    @staticmethod
    def get_manual_date():
        manual_date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
        if not manual_date:
            manual_date = date.today().strftime("%Y-%m-%d")
        return manual_date
