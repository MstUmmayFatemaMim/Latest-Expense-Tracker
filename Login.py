from Config import AllConnection


class Login:
    @staticmethod
    def login_page():
        print("*" * 12, "   Welcome to Our Login Page  ", "*" * 12)
        user_name = input("Enter your name: ")
        password = input("Enter your password: ")
        all_user = AllConnection.read_data(AllConnection.User_File_Path)
        for user in all_user:
            if user_name == user["user_name"] and password == user["password"]:
                print("*" * 12, "   Login Successfully  ", "*" * 12)
                return user
        print("Wrong name or password!")
        return None
