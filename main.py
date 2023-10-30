from src.menu.check_birthday_menu import check_birthday_menu
from src.utils.contact_book.contact_book_manager import ContactBookManager
from src.utils.notes_book.notes_book_manager import NotesBookManager
from src.menu.contact_menu import contact_menu
from src.menu.note_menu import notes_menu


def main():
    contact_book_manager = ContactBookManager()
    notes_book_manager = NotesBookManager()
    while True:
        print("\n===== Main Menu =====")
        print("1. Manage Contacts")
        print("2. Manage Notes")
        print("3. Check Days Until Next Birthday")
        print("4. Exit Program")
        choice = str(input("Choose option (1/2/3/4): "))
        if choice == '1':
            contact_menu(contact_book_manager)
        elif choice == '2':
            notes_menu(notes_book_manager)
        elif choice == '3':
            check_birthday_menu(contact_book_manager)
        elif choice == '4':
            print("Closing the program. Goodbye!")
            break
        else:
            print("Invalid choice. Choose an option from 1 to 3.")


if __name__ == '__main__':
    main()
