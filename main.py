from src.mongodb.db_manager import DatabaseManager
from src.models import AdressBook, NoteBook
import re
from datetime import datetime


# Wszystkie zdaerzenia wykonane w tym programie maja byc zapisywane w pliku na dysku twardym.


# Na pocztaku chcemy dodac nowy kontakt do naszej ksiazki kontaktow.
# Kontakt ma sie skladac z Imienia i Nazwiska, numeru telefonu, adrsu e-mail oraz daty urodzin.
# Kontakty musza byc zapisywane w zewnetrzym pliku.


# Chcemy miec mozliwosc wyszukiwania kontaktow z naszej ksiazki telefonicznej.


# Chcemy tez miec mozliwosc edytowania kontaktu.


# Chcemy miec mozliwosc usuniecia kontaktu z naszej listy.


# Przy wprowadzaniu takich danych jak numer, telefonu, adresu e-mail czy daty urodzenia,
#  ma wyskakiwac blad gdy dane beda nieprawidlowe.
def validate_phone_number(func):
    def wrapper(*args, **kwargs):
        phone_number = args[2]
        pattern = r"\d{9}"
        if re.match(pattern, phone_number):
            return func(*args, **kwargs)
        else:
            return f'Wrong phone number. Sample number: "123456789"'
    return wrapper

def validate_e_mail(func):
    def wrapper(*args, **kwargs):
        e_mail = args[3]
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern, e_mail):
            return func(*args, **kwargs)
        else:
            return f'Bad email. Example email address: "silmple_adres@ios.com"'
    return wrapper

def is_valid_date(func):
    def wrapper(*args, **kwargs):
        birthday = args[4]
        try:
            datetime.strptime(birthday, '%Y-%m-%d')
            return func(*args, **kwargs)
        except ValueError:
            return f'Wrong date of birth. Correct format "yyyy-mm-dd"'
    return wrapper


# Chcemy miec mozliwosc sprawdzenia ile czy ktos ma urodziny w ciagu najblizszych 30 dni
# badz tez wypisac liste wszystykich urodzin sortujac od najblizszych.

# Druga sprawa to mozliwosc dodawanie notatek do naszego notesu.
# Notatka ma sie skladac dwoch rzeczy: 'Tag' oraz przedmiotu notatki.
# Przedmiotem notatki moze byc informacja tekstowa, obraz, dokument, film itp.
# Notatki musza byc zapisywane w pliku zewnatrzym.
class Note:
    def __init__(self, title, tag, content):
        self.title = title
        self.tag = tag
        self.content = content

    def add_note(self):
        pass
# Dodawanie notatek do notbook.

    def edit_note(self):
        pass
# Edycja notatek

    def remove_note(self):
        pass
# Usuwanie notatek

    def sort_note(self):
        pass
# Sortowanie notatek po tytule, badz tagach.



# Stworzenie interfejsu poruszania sie po terminalu.


def main():
    #TEST
    db = DatabaseManager()
    db.show_all(AdressBook)
    print('\n')
    db.show_all(NoteBook)

    #dodawanie danych do BD

    # dodanie do kolekcji adress_book
    # contact = AdressBook(imie="Adam", nazwisko='Smith', numer_telefonu="123-456-789", email="smith@email.com", data_urodzin="01-01-2000")
    #db.add(contact)

    # dodanie do kolekcji note_book
    # note = NoteBook(tytul="My Note", tresc="This is a note.", tagi=["tag1", "tag2"])
    # db.add(note)


if __name__ == '__main__':
    main()
