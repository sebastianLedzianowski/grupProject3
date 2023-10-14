from src.utils.contact_book.contact_book_collector import ContactBookCollector
from src.utils.contact_book.contact_book_manager import ContactBookManager
from src.utils.notes_book.notesbook_collector import NotesBookCollector
from src.utils.notes_book.notesbook_manager import NotesBookManager
def test_add_contact():
    user_data = ContactBookCollector().get_user_input()
    ContactBookManager().create(user_data=user_data)

def test_add_note():
    user_data = NotesBookCollector().get_user_input()
    NotesBookManager().create(user_data=user_data)



if __name__ == '__main__':
    # test_add_contact()
    # test_add_note()