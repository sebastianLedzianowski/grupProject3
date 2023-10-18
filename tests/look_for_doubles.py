from src.utils.contact_book.contact_book_manager import ContactBookManager
from src.utils.notes_book.notesbook_manager import NotesBookManager
from src.utils.data_decorators import *
from tests.read_all_notes_book import read_all_notes_book
from tests.read_all_contact_book import read_all_contact_book

def doubles_notes(key, value):
    return NotesBookManager().look_for_doubles(key,value)
def doubles_contacts(key, value):
    return ContactBookManager().look_for_doubles(key,value)

if __name__ == '__main__':
    #read_all_notes_book()
    #read_all_contact_book()
    
    print(doubles_contacts("name", "Tadeo"))
    print(doubles_notes("title","Fancy title"))