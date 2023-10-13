from src.mongodb.db_connection import DatabaseConnectionManager
from src.mongodb.db_repository import DataRepository
from src.mongodb.models import AddressBook, NoteBook
from faker import Faker
import random

fake = Faker("pl_PL")
db_manager = DatabaseConnectionManager()
data_repo = DataRepository(db_manager)


def faker_Notesbook():
    for _ in range(20):
        rekord = NoteBook(
            title=fake.sentence(),
            tag=[fake.word() for _ in range(random.randint(1, 5))],
            content=fake.paragraph()
        )
        print(f"Title: {rekord.title}\n"
              f"Tag: {rekord.tag}\n"
              f"Content: {rekord.content}\n")


def faker_AdressBook():
    for _ in range(20):
        rekord = AddressBook(
            name=fake.first_name(),
            surname=fake.last_name(),
            phone_number=fake.numerify(text='#########'),
            email=fake.email(),
            birthday=fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d')
        )
        print(rekord)


if __name__ == '__main__':
    faker_AdressBook()
    print()
    print('-'*140)
    print()
    faker_Notesbook()
