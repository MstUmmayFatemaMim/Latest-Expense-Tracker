from Config import AllConnection


class Registration:

    @staticmethod
    def registration_page():
        print("*" * 12, "   Welcome to Our Registration Page  ", "*" * 12)
        user_name = input("Enter your name: ")
        password = input("Enter your password: ")
        user_id = input("Enter your id: ")

        user_data = {
            "user_name": user_name,
            "password": password,
            "user_id": user_id
        }

        AllConnection.write_and_save_data(
            AllConnection.User_File_Path,
            AllConnection.User_Column,
            user_data
        )
        print("*" * 12, "   Thank you for registering  ", "*" * 12)
        return user_data
