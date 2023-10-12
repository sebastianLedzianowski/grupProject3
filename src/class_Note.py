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


