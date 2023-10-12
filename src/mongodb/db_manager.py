from pymongo import MongoClient
from dotenv import load_dotenv
from src.models import AdressBook, NoteBook
from typing import Type, List, Union
from dataclasses import asdict
import os


class DatabaseManager:
    def __init__(self):
        """
        Inicjalizacja managera bazy danych.
        Łączy się z bazą używając adresu z pliku .env.
        """

        load_dotenv()
        self.url = os.getenv("DB_URL")
        self.client = MongoClient(self.url)
        self.db = self.client['db_project3']
        self.adress_book = self.db["adress_book"]
        self.note_book = self.db["note_book"]

    def show_all(self, value: Type[Union[AdressBook, NoteBook]]) -> List[Union[AdressBook, NoteBook]]:
        """
        Wyświetla wszystkie wpisy z wybranej kolekcji (książka adresowa lub notatnik).

        Args:
        - value (Type[Union[AdressBook, NoteBook]]): Typ modelu na podstawie, którego wybierana jest kolekcja.

        Returns:
        - List[Union[AdressBook, NoteBook]]: Lista obiektów z wybranej kolekcji.
        """
        if value == AdressBook:
            collection = self.adress_book
            return [i for i in collection.find()]

        if value == NoteBook:
            collection = self.note_book
            return [i for i in collection.find()]

    def add(self, value: Union[AdressBook, NoteBook]):
        """
        Dodaje nowy wpis do odpowiedniej kolekcji w bazie danych.

        Args:
        - value (Union[AdressBook, NoteBook]): Obiekt AdressBook lub NoteBook do dodania.

        Returns:
        - ObjectId: ID dodanego wpisu.
        """
        if isinstance(value, AdressBook):
            collection = self.adress_book
        elif isinstance(value, NoteBook):
            collection = self.note_book
        else:
            raise ValueError('Nie ma takiej bazy o danej nazwie.')

        return collection.insert_one(asdict(value)).inserted_id



db = DatabaseManager()



print(db.show_all(AdressBook))








