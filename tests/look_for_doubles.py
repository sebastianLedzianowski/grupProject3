from src.utils.contact_book.contact_book_manager import ContactBookManager
from src.utils.notes_book.notesbook_manager import NotesBookManager
from tests.read_all_notes_book import *

def read_all_contact_book():
    notes_manager = ContactBookManager()
    notes = notes_manager.read_all()
    if notes:
        print(f"here is the contact list:")
        for note in notes:
            print(note)
    else:
        print(f'No notes in the database.')

def doubles_notes(key, value):
    return NotesBookManager().look_for_doubles(key, value)
def doubles_contacts(key, value):
    return ContactBookManager().look_for_doubles(key, value)

if __name__ == '__main__':
    read_all_notes_book()
    