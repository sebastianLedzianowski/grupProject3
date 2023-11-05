from src.menu.abstractmethod_models import UserInterface

class MainMenu(UserInterface):
    def display(self):
        print("\n===== Main Menu =====")
        print("1. Manage Contacts")
        print("2. Manage Notes")
        print("3. Check Days Until Next Birthday")
        print("4. Exit Program")

    def user_choice(self):
        return str(input("Choose option (1/2/3/4): "))