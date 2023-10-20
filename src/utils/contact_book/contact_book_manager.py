from src.mongodb.db_connection import DatabaseConnectionManager
from src.mongodb.db_repository import DataRepository
from src.mongodb.models import AddressBook
from datetime import datetime, timedelta, date
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
            self.data_repo.update(value_type=AddressBook, field=field, value=value, updates=updates)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def edit_by_criteria(self, search_criteria, updates):
        try:
            self.data_repo.update_by_criteria(value_type=AddressBook, search_criteria=search_criteria, updates=updates)
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

    def look_for_doubles(self, field, value):
        try:
            notes = self.data_repo.read_all(AddressBook)
            duplicates = []

            for note_dict in notes:
                if note_dict.get(field) == value:
                    duplicates.append(note_dict)

            if len(duplicates) > 1:
                return duplicates
            else:
                return None

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    @property
    def get_days_to_birthday(self):
        today = date.today()
        today_to_30 = today + timedelta(days=30)
        contacts = self.data_repo.read_all(AddressBook)
        upcoming_birthdays = []
        for contact in contacts:
            birthday = datetime.strptime(contact["birthday"], "%Y-%m-%d")
            upcoming_birthday = date(today.year, birthday.month, birthday.day)
            days_to_birthdays = (upcoming_birthday - today).days
            if today.day == birthday.day and today.month == birthday.month:
                upcoming_birthdays.append({"name": contact['name'],
                                           "surname": contact['surname'],
                                           "birthday": contact['birthday'],
                                           "email": contact['email'],
                                           "days_to_birthday": days_to_birthdays
                                           })
            if today < upcoming_birthday <= today_to_30:
                upcoming_birthdays.append({"name": contact["name"],
                                           "surname": contact["surname"],
                                           "birthday": contact["birthday"],
                                           "days_to_birthday": days_to_birthdays
                                           })
        sorted_upcoming_birthdays = sorted(upcoming_birthdays, key=lambda x: -x["days_to_birthday"])
        return sorted_upcoming_birthdays

    @staticmethod
    def get_birthday_wish(name):
        url = os.getenv("BIRTHDAY_URL")
        data = {"name": name}
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=data, headers=headers)
        return response
