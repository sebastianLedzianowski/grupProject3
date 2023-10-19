from src.mongodb.db_connection import DatabaseConnectionManager
from src.mongodb.db_repository import DataRepository
from src.utils.contact_book.contact_book_manager import ContactBookManager
from src.utils.notes_book.notesbook_manager import NotesBookManager
from faker import Faker
import random

fake = Faker("pl_PL")
db_manager = DatabaseConnectionManager()
data_repo = DataRepository(db_manager)


def faker_notes_book():
    notes_manager = NotesBookManager()
    for _ in range(20):
        dictionary_record = {
            'title': fake.sentence(),
            'tag': [fake.word() for _ in range(random.randint(1, 5))],
            'content': fake.paragraph()
        }
        print(dictionary_record)
        notes_manager.create(user_data=dictionary_record)

def faker_contacts_book():
    contacts_manager = ContactBookManager()
    for _ in range(20):
        dictionary_record = {
            'name': fake.first_name(),
            'surname': fake.last_name(),
            'phone_number': fake.phone_number(),
            'email': fake.email(),
            'birthday': fake.date_of_birth(minimum_age=18, maximum_age=50).strftime('%Y-%m-%d'),
        }
        print(dictionary_record)
        contacts_manager.create(user_data=dictionary_record)


if __name__ == '__main__':
    faker_notes_book()
    print()
    print('-'*140)
    print()
    faker_contacts_book()
