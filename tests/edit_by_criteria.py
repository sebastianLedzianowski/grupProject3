from src.utils.contact_book.contact_book_collector import ContactBookCollector
from src.utils.contact_book.contact_book_manager import ContactBookManager
from tests.look_for_doubles import *

def read_all_contacts_book():
    notes_manager = ContactBookManager()
    notes = notes_manager.read_all()
    if notes:
        print(f"here is the contact list:")
        for note in notes:
            print(note)
    else:
        print(f'No notes in the database.')


def test_edit(search_criteria, updates):
    ContactBookManager().edit_by_criteria(search_criteria, updates)

if __name__ == '__main__':
    read_all_contacts_book()
    doubles = doubles_contacts("name", "Barbara")
    choice = 1
    _id = doubles[choice - 1]["_id"]
    test_edit({"_id":_id}, {"name": "Basia"})
    read_all_contacts_book()