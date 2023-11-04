from src.menu.console_interface.main_menu import MainMenu
from src.menu.console_interface.check_birthday_menu import check_birthday_menu
from src.menu.console_interface.manage_contacts import ManageContactsABC, SortContactsABC, ChooseContactABC, \
    ContactEditDeleteMenuABC
from src.menu.console_interface.manage_notes import ManageNotesABC, SortChoiceABC, ChooseNoteABC, NoteEditDeleteMenuABC
from src.utils.contact_book.contact_book_manager import ContactBookManager
from src.utils.notes_book.notes_book_manager import NotesBookManager
from src.menu.console_interface.contact_menu import contact_menu
from src.menu.console_interface.note_menu import notes_menu


def main(user_interface):
    contact_book_manager = ContactBookManager()
    notes_book_manager = NotesBookManager()
    manage_contacts_abc = ManageContactsABC()
    sort_contacts_abc = SortContactsABC()
    choose_contact_abc = ChooseContactABC()
    contact_edit_delete_menu_abc = ContactEditDeleteMenuABC()
    manage_notes_abc = ManageNotesABC()
    sort_choice_abc = SortChoiceABC()
    choose_note_abc = ChooseNoteABC()
    note_edit_delete_menu_abc = NoteEditDeleteMenuABC()
    while True:
        user_interface.display()
        choice = user_interface.user_choice()
        if choice == '1':
            contact_menu(contact_book_manager, user_interface, manage_contacts_abc, sort_contacts_abc,
                         choose_contact_abc, contact_edit_delete_menu_abc)
        elif choice == '2':
            notes_menu(notes_book_manager, user_interface, manage_notes_abc, sort_choice_abc, choose_note_abc,
                       note_edit_delete_menu_abc)
        elif choice == '3':
            check_birthday_menu(contact_book_manager, user_interface)
        elif choice == '4':
            user_interface.display_print("Closing the program. Goodbye!")
            break
        else:
            user_interface.display_print("Invalid choice. Choose an option from 1 to 4.")


if __name__ == '__main__':
    console_interface = MainMenu()
    main(console_interface)
