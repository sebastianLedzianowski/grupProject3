from src.mongodb.db_manager import DatabaseManager

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
class Note:
    def __init__(self, title, tag, content):
        self.title = title
        self.tag = tag
        self.content = content

    def add_note(self):
# Dodawanie notatek do notbook.

    def edit_note(self):
# Edycja notatek

    def remove_note(self):
# Usuwanie notatek

    def sort_note(self):
# Sortowanie notatek po tytule, badz tagach.



# Stworzenie interfejsu poruszania sie po terminalu.


def main():
    print('db test')
    DatabaseManager().show_all()


if __name__ == '__main__':
    main()
