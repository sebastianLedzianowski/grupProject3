from src.mongodb.db_connection import DatabaseConnectionManager
from src.mongodb.db_repository import DataRepository

db_manager = DatabaseConnectionManager()
data_repo = DataRepository(db_manager)

class Note:
    def __init__(self, title, tag, content):
        self.title = title
        self.tag = tag
        self.content = content

class NotesBook(Note):
    def __init__(self, title, tag, content):
        super().__init__(title, tag, content)
    def create(self):
        pass
    # Dodawanie notatek do notbook.

    def read(self):
        pass
    # Wyswietlanie notatek po tytule, badz tagach.

    def sort(self):
        pass
    # Sortowanie notatek po danym argumencie.
    def edit(self):
        pass
    # Edycja notatek

    def delate(self):
        pass
    # Usuwanie notatek
