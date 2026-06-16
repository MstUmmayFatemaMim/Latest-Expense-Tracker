from Login import Login
from Registration import Registration
from Dashboard import DashBoard

register_user = Registration()
log_user = Login()


def showlist():
    print("*" * 12, "   Welcome to Our Expense Tracker  ", "*" * 12)
    print("1. Create a new account")
    print("2. Log in")
    print("3. Log out")
    print("4. Exit")
    print("*" * 50)


while True:
    showlist()
    choice = input("Enter your choice: ")
    if choice == "1":
        reg_user = register_user.registration_page()
        if reg_user:
            DashBoard(reg_user).dashboard()
    elif choice == "2":
        logged_user = log_user.login_page()
        if logged_user:
            DashBoard(logged_user).dashboard()
    elif choice == "3":
        print("Log out")
        break
    elif choice == "4":
        print("Exit")
        break
    else:
        print("Invalid choice")
