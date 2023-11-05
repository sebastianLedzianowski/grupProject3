from src.menu.abstractmethod_models import UserInterface

class ManageContactsABC(UserInterface):
    def display(self):
        print("\n===== Manage Contacts =====")
        print("1. Display Contacts")
        print("2. Add Contact")
        print("3. Choose Contact to edit/delete")
        print("4. Sort Contacts")
        print("5. Back to Main Menu")

    def user_choice(self):
        return str(input("Choose option (1/2/3/4/5): "))

class SortContactsABC(UserInterface):
    def display(self):
        print("\n===== Sort Contacts =====")
        print("1. Sort by Name")
        print("2. Sort by Surname")
        print("3. Sort by Phone number")
        print("4. Sort by Email")
        print("5. Sort by Birthday")
        print("6. Back to Manage Contacts")

    def user_choice(self):
        return str(input("Choose sort option (1/2/3/4/5/6): "))

class ChooseContactABC(UserInterface):
    def display(self):
        print("\n===== Choose Contact by =====")
        print("1. Choose by Name")
        print("2. Choose by Surname")
        print("3. Choose by Phone number")
        print("4. Choose by Email")
        print("5. Choose by Birthday")
        print("6. Back to Manage Contacts Menu")

    def user_choice(self):
        return str(input("Choose edit option (1/2/3/4/5/6): "))

class ContactEditDeleteMenuABC(UserInterface):
    def display(self):
        print("\n===== Choose option =====")
        print("1. Edit Contact")
        print("2. Delete Contact")
        print("3. Back to Manage Contacts")

    def user_choice(self):
        return str(input("Choose option (1/2/3): "))