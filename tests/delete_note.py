from src.utils.contact_book.contact_book_collector import ContactBookCollector
from src.utils.contact_book.contact_book_manager import ContactBookManager
from src.utils.notes_book.notesbook_collector import NotesBookCollector
from src.utils.notes_book.notesbook_manager import NotesBookManager
from src.utils.data_decorators import *
from tests.read_all_notes_book import read_all_notes_book

def test_delete(key, value):
    NotesBookManager().delete(key,value)


if __name__ == '__main__':
    read_all_notes_book()
    test_delete("title", "")
    read_all_notes_book()
    