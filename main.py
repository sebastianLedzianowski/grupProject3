from src.mongodb.db_manager import DatabaseManager
from src.models import AdressBook, NoteBook


# Wszystkie zdaerzenia wykonane w tym programie maja byc zapisywane w pliku na dysku twardym.


# Na pocztaku chcemy dodac nowy kontakt do naszej ksiazki kontaktow.
# Kontakt ma sie skladac z Imienia i Nazwiska, numeru telefonu, adrsu e-mail oraz daty urodzin.
# Kontakty musza byc zapisywane w zewnetrzym pliku.


# Chcemy miec mozliwosc wyszukiwania kontaktow z naszej ksiazki telefonicznej.


# Chcemy tez miec mozliwosc edytowania kontaktu.


# Chcemy miec mozliwosc usuniecia kontaktu z naszej listy.


# Przy wprowadzaniu takich danych jak numer, telefonu, adresu e-mail czy daty urodzenia,
#  ma wyskakiwac blad gdy dane beda nieprawidlowe.


# Chcemy miec mozliwosc sprawdzenia ile czy ktos ma urodziny w ciagu najblizszych 30 dni
# badz tez wypisac liste wszystykich urodzin sortujac od najblizszych.

# Druga sprawa to mozliwosc dodawanie notatek do naszego notesu.
# Notatka ma sie skladac dwoch rzeczy: 'Tag' oraz przedmiotu notatki.
# Przedmiotem notatki moze byc informacja tekstowa, obraz, dokument, film itp.
# Notatki musza byc zapisywane w pliku zewnatrzym.


# Edycja notatek


# Usuwanie notatek


# Stworzenie interfejsu poruszania sie po terminalu.


def main():
    #TEST
    db = DatabaseManager()
    #dodawanie danych do BD

    # dodanie do kolekcji adress_book
    # contact = AdressBook(imie="Adam", nazwisko='Smith', numer_telefonu="123456789", email="smith@email.com", data_urodzin="2000-01-01")
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

    db.show_all(AdressBook)


if __name__ == '__main__':
    main()
