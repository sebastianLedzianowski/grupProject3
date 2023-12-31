from src.menu.console_interface.check_birthday_menu import check_birthday_menu
from src.menu.console_interface.abstractmethod.manage_contacts import ManageContactsABC, SortContactsABC, \
    ChooseContactABC, ContactEditDeleteMenuABC
from src.menu.console_interface.abstractmethod.manage_notes import ManageNotesABC, SortChoiceABC, ChooseNoteABC, \
    NoteEditDeleteMenuABC
from src.utils.contact_book.contact_book_manager import ContactBookManager
from src.utils.notes_book.notes_book_manager import NotesBookManager
from src.menu.console_interface.contact_menu import contact_menu
from src.menu.console_interface.note_menu import notes_menu

def console_interface_main(user_interface):
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
        match choice:
            case '1':
                contact_menu(contact_book_manager, user_interface, manage_contacts_abc, sort_contacts_abc,
                             choose_contact_abc, contact_edit_delete_menu_abc)
            case '2':
                notes_menu(notes_book_manager, user_interface, manage_notes_abc, sort_choice_abc, choose_note_abc,
                           note_edit_delete_menu_abc)
            case '3':
                check_birthday_menu(contact_book_manager, user_interface)
            case '4':
                user_interface.display_print("Closing the program. Goodbye!")
                break
            case _:
                user_interface.display_print("Invalid choice. Choose an option from 1 to 4.")