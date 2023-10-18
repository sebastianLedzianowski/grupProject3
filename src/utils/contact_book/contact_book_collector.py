from dataclasses import asdict
from src.mongodb.models import AddressBook
from src.utils.data_decorators import *


class ContactBookCollector:
    @staticmethod
    @validate_input("Enter name: ")
    def get_name():
        pass

    @staticmethod
    @validate_input("Enter surname: ")
    def get_surname():
        pass

    @staticmethod
    @validate_phone_number
    def get_phone_number():
        pass

    @staticmethod
    @validate_email
    def get_email():
        pass

    @staticmethod
    @validate_date
    def get_birthday():
        pass

    @staticmethod
    def get_user_input():
        name = ContactBookCollector.get_name()
        surname = ContactBookCollector.get_surname()
        phone_number = ContactBookCollector.get_phone_number()
        email = ContactBookCollector.get_email()
        birthday = ContactBookCollector.get_birthday()

        address_book_entry = AddressBook(
            name=name,
            surname=surname,
            phone_number=phone_number,
            email=email,
            birthday=birthday
        )

        return asdict(address_book_entry)
