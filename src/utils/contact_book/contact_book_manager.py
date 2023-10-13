from src.mongodb.db_connection import DatabaseConnectionManager
from src.mongodb.db_repository import DataRepository
from src.mongodb.models import AddressBook


class ContactBookManager:
    def __init__(self):
        self.db_manager = DatabaseConnectionManager()
        self.data_repo = DataRepository(self.db_manager)

    def add(self, user_data):
        try:
            self.data_repo.create(AddressBook(name=user_data['name'],
                                              surname=user_data['surname'],
                                              phone_number=user_data['phone_number'],
                                              email=user_data['email'],
                                              birthday=user_data['birthday']))
        except Exception as e:
            print(f"An error occurred: {str(e)}")
