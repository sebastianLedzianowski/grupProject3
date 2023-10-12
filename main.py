from src.mongodb.db_manager import DatabaseManager
from src.models import AdressBook, NoteBook
from src.data_decorators import *
from datetime import datetime
import re

import random

# Chcemy miec mozliwosc sprawdzenia ile czy ktos ma urodziny w ciagu najblizszych 30 dni
# badz tez wypisac liste wszystykich urodzin sortujac od najblizszych.


# Stworzenie interfejsu poruszania sie po terminalu.


def main():
    #TEST
    db = DatabaseManager()
    #dodawanie danych do BD

    # dodanie do kolekcji adress_book
    # contact = AdressBook(imie="Adam", nazwisko='Smith', numer_telefonu="123456789", email="smith@email.com", data_urodzin="2001-01-01")
    #db.add(contact)

    # dodanie do kolekcji note_book
    # note = NoteBook(tytul="My Note", tresc="This is a note.", tagi=["tag1", "tag2"])
    # db.add(note)


    # edycja danych w BD
    # chcemy na przyklad zmienic numer telefonu dla Smith
    # tworzymy slownik ze zmiana konkretnej danej.
    # updates = {'numer_telefonu': '987654321'}
    # # wprowadzeenie zmian w BD po nazwisku
    # db.edit(AdressBook, 'nazwisko', 'Smith', updates)
    # print('\n')



if __name__ == '__main__':
    main()
