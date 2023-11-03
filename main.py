from src.menu.console_interface.MainMenu import MainMenu
from src.menu.check_birthday_menu import check_birthday_menu
from src.menu.console_interface.Manage_Contacts import ManageContactsABC, SortContactsABC, ChooseContactABC, \
    ContactEditDeleteMenuABC
from src.utils.contact_book.contact_book_manager import ContactBookManager
from src.utils.notes_book.notes_book_manager import NotesBookManager
from src.menu.contact_menu import contact_menu
from src.menu.note_menu import notes_menu


def main(user_interface):
    contact_book_manager = ContactBookManager()
    notes_book_manager = NotesBookManager()
    manage_contacts_abc = ManageContactsABC()
    sort_contacts_abc = SortContactsABC()
    choose_contact_abc = ChooseContactABC()
    contact_edit_delete_menu_abc = ContactEditDeleteMenuABC()
    while True:
        user_interface.display()
        choice = user_interface.user_choice()
        if choice == '1':
            contact_menu(contact_book_manager, user_interface, manage_contacts_abc, sort_contacts_abc, choose_contact_abc,
                         contact_edit_delete_menu_abc)
        elif choice == '2':
            notes_menu(notes_book_manager, user_interface)
        elif choice == '3':
            check_birthday_menu(contact_book_manager, user_interface)
        elif choice == '4':
            user_interface.display("Closing the program. Goodbye!")
            break
        else:
            user_interface.display("Invalid choice. Choose an option from 1 to 3.")


if __name__ == '__main__':
    console_interface = MainMenu()
    main(console_interface)
