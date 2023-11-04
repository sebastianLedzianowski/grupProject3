from src.menu.console_interface.abstractmethod.models import UserInterface

class ManageNotesABC(UserInterface):
    def display(self):
        print("\n===== Manage Notes =====")
        print("1. Display Notes")
        print("2. Add Note")
        print("3. Choose Note to Edit/Delete")
        print("4. Sort Notes")
        print("5. Back to Main Menu")

    def user_choice(self):
        return str(input("Choose option (1/2/3/4/5/6): "))

class SortChoiceABC(UserInterface):
    def display(self):
        print("\n===== Sort Notes =====")
        print("1. Sort by Title")
        print("2. Sort by Tag")
        print("3. Sort by Content")
        print("4. Back to Manage Notes")

    def user_choice(self):
        return str(input("Choose sort option (1/2/3/4): "))

class ChooseNoteABC(UserInterface):
    def display(self):
        print("\n===== Choose Note by =====")
        print("1. Choose by Title")
        print("2. Choose by Tag")
        print("3. Choose by Content")
        print("4. Back to Manage Notes Menu")

    def user_choice(self):
        return str(input("Choose edit option (1/2/3/4): "))

class NoteEditDeleteMenuABC(UserInterface):
    def display(self):
        print("\n===== Choose option =====")
        print("1. Edit Note")
        print("2. Delete Note")
        print("3. Back to Manage Notes")

    def user_choice(self):
        return str(input("Choose option (1/2/3): "))