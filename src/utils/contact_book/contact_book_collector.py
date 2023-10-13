from dataclasses import asdict
from src.mongodb.models import AddressBook


class ContactBookCollector:
    @staticmethod
    def get_user_input():
        name = input('Enter name: ')
        surname = input('Enter surname: ')
        phone_number = input('Enter phone number: ')
        email = input('Enter email: ')
        birthday = input('Enter birthday [YYYY-MM-DD]: ')

        address_book_entry = AddressBook(
            name=name,
            surname=surname,
            phone_number=phone_number,
            email=email,
            birthday=birthday
        )

        return asdict(address_book_entry)
