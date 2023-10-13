from src.mongodb.db_connection import DatabaseConnectionManager
from src.mongodb.db_repository import DataRepository
from src.mongodb.models import AddressBook, NoteBook
from src.utils.contact_book.contact_book_collector import ContactBookCollector
from src.utils.contact_book.contact_book_manager import ContactBookManager


def main():
    # userdata=ContactBookCollector().get_user_input()
    # ContactBookManager().create(user_data=userdata)
    date=ContactBookManager().read_all()
    print(date)




if __name__ == '__main__':
    main()
