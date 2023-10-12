from pymongo import MongoClient
from dotenv import load_dotenv
from src.mongodb.models import AdressBook, NoteBook
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

    def show_all(self, value_type: Type[Union[AdressBook, NoteBook]]) -> List[Union[AdressBook, NoteBook]]:
        """
        Wyświetla wszystkie wpisy z wybranej kolekcji (książka adresowa lub notatnik).

        Args:
        - value (Type[Union[AdressBook, NoteBook]]): Typ modelu na podstawie, którego wybierana jest kolekcja.

        Returns:
        - List[Union[AdressBook, NoteBook]]: Lista obiektów z wybranej kolekcji.
        """
        if value_type == AdressBook:
            collection = self.adress_book
            return [i for i in collection.find()]

        if value_type == NoteBook:
            collection = self.note_book
            return [i for i in collection.find()]

    def add(self, value_type: Union[AdressBook, NoteBook]):
        """
        Dodaje nowy wpis do odpowiedniej kolekcji w bazie danych.

        Args:
        - value (Union[AdressBook, NoteBook]): Obiekt AdressBook lub NoteBook do dodania.

        Returns:
        - ObjectId: ID dodanego wpisu.
        """

        # Wybór odpowiedniej kolekcji
        if isinstance(value_type, AdressBook):
            collection = self.adress_book
        elif isinstance(value_type, NoteBook):
            collection = self.note_book
        else:
            raise ValueError('Nie ma takiej bazy o danej nazwie.')

        return collection.insert_one(asdict(value_type)).inserted_id

    def edit(self, value_type: Type[Union[AdressBook, NoteBook]], field: str, value: str, updates: dict):
        """
        Edytuje wartości w rekordzie wybranym po danym polu.

        Args:
        - value_type (Type[Union[AdressBook, NoteBook]]): Typ rekordu do edycji.
        - field (str): Pole do wyszukania (np. 'nazwisko' dla AdressBook).
        - value (str): Wartość do wyszukania.
        - updates (dict): Słownik z aktualizacjami.

        Returns:
        - UpdateResult: Wynik operacji aktualizacji.
        """

        # Wybór odpowiedniej kolekcji
        if value_type == AdressBook:
            collection = self.adress_book
        elif value_type == NoteBook:
            collection = self.note_book
        else:
            raise ValueError('Nie ma takiej bazy o danej nazwie.')

        # Znajdz wszystrkie rekord z daną wartością
        records = list(collection.find({field: value}))

        if not records:
            print(f'Nie znaleziuono żadnego rekordu z {field}: {value}')
            return

        if len(records) > 1:
            print(f'Znaleziono kilka rekordów z {field}: {value}')
            for i, record in enumerate(records, 1):
                if value_type == AdressBook:
                    print(f"{i}. {record['imie']} {record['nazwisko']} - {record['email']}")
                elif value_type == NoteBook:
                    print(f"{i}. {record['tytul']} - Tagi: {', '.join(record['tagi'])}")

            choice = int(input(f'Wybierz numer rekordu do edycji (1-{len(records)}): '))
            if choice < 1 or choice > len(records):
                print('Nieprawidłowy wybór.')
                return
            record_to_edit = records[choice - 1]
        else:
            record_to_edit = records[0]

        # Aktualizuj wybrany rekord
        result = collection.update_one({'_id': record_to_edit['_id']}, {"$set": updates})
        return result
