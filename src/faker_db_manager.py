from src.mongodb.db_manager import DatabaseManager
from src.models import AdressBook, NoteBook
from faker import Faker
import random

fake = Faker()
baza_danych = DatabaseManager

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
        rekord = AdressBook(
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