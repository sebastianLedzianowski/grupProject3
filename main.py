from src.mongodb.db_connection import DatabaseConnectionManager
from src.mongodb.db_repository import DataRepository
from src.mongodb.models import AddressBook, NoteBook
from src.utils.contact_book.contact_book_collector import ContactBookCollector
from src.utils.contact_book.contact_book_manager import ContactBookManager

user_data = ContactBookCollector().get_user_input()
ContactBookManager().add(user_data=user_data)
def main():
    # TEST
    # Initialize the database connection and data repository
    db_manager = DatabaseConnectionManager()
    data_repo = DataRepository(db_manager)

    for contact in data_repo.read_all(AddressBook):
        print(f"Name: {contact['name']}, Surname: {contact['surname']}, Phone number: {contact['phone_number']},"
              f" Email: {contact['email']}, Birthday: {contact['birthday']}\n")
    print()
    print("-"*130)
    print()
    for note in data_repo.read_all(NoteBook):
        print(f"Title: {note['title']}, Tag: {note['tag']}\nContent: {note['content']}\n")


if __name__ == '__main__':
    main()
