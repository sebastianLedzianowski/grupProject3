from src.mongodb.db_manager import DatabaseManager
from src.mongodb.models import AdressBook, NoteBook
from src.faker_db_manager import faker_Notesbook, faker_AdressBook
from src.data_decorators import *
from datetime import datetime
import re


# Chcemy miec mozliwosc sprawdzenia ile czy ktos ma urodziny w ciagu najblizszych 30 dni
# badz tez wypisac liste wszystykich urodzin sortujac od najblizszych.


# Stworzenie interfejsu poruszania sie po terminalu.


def main():
    #TEST
    db = DatabaseManager()

    # dodawanie danych do BD

    # dodanie do kolekcji adress_book
    # contact = AdressBook(name="Adam", surname="Smith", phone_number="123456789", email="smith@email.com", birthday="2001-01-20")
    # db.add(contact)

    # dodanie do kolekcji note_book
    # note = NoteBook(title="My Note", content="This is a note.", tag=["tag1", "tag2"])
    # db.add(note)


    # edycja danych w BD
    # chcemy na przyklad zmienic numer telefonu dla Smith
    # tworzymy slownik ze zmiana konkretnej danej.
    # updates = {'numer_telefonu': '987654321'}
    # # wprowadzeenie zmian w BD po nazwisku
    # db.edit(AdressBook, 'nazwisko', 'Smith', updates)
    # print('\n')

    for contact in db.show_all(AdressBook):
        print(f"Name: {contact['name']}, Surname: {contact['surname']}, Phone number: {contact['phone_number']},"
              f" Email: {contact['email']}, Birthday: {contact['birthday']}\n")
    print()
    print("-"*130)
    print()
    for note in db.show_all(NoteBook):
        print(f"Title: {note['title']}, Tag: {note['tag']}\nContent: {note['content']}\n")

if __name__ == '__main__':
    main()
#test t1
#test t2
