from src.mongodb.db_connection import DatabaseConnectionManager
from src.mongodb.db_repository import DataRepository
from src.mongodb.models import AddressBook
from dotenv import load_dotenv
import requests
import os


class ContactBookManager:
    def __init__(self):
        self.db_manager = DatabaseConnectionManager()
        self.data_repo = DataRepository(self.db_manager)
        load_dotenv()

    def create(self, user_data):
        try:
            self.data_repo.create(AddressBook(name=user_data['name'],
                                              surname=user_data['surname'],
                                              phone_number=user_data['phone_number'],
                                              email=user_data['email'],
                                              birthday=user_data['birthday']))
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def edit(self, field, value, updates):
        try:
            self.data_repo.update(value_type=AddressBook, field=field, value=value, updates={"$set": {field: updates}})
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def delete(self, field, value):
        try:
            self.data_repo.delete(value_type=AddressBook, field=field, value=value)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def read_all(self) -> list:
        try:
            all_documents = self.data_repo.read_all(AddressBook)
            return list(all_documents)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return []

    def get_sorted_contacts(self, sort_key) -> list:
        try:
            contacts = self.data_repo.read_all(AddressBook)
            sorted_contacts = sorted(contacts, key=lambda x: x.get(sort_key, ""))
            return sorted_contacts
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return []

    @staticmethod
    def get_birthday_wish(name):
        url = os.getenv("BIRTHDAY_URL")
        data = {"name": name}
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=data, headers=headers)
        return response
