from src.mongodb.db_connection import DatabaseConnectionManager
from src.mongodb.db_repository import DataRepository

db_manager = DatabaseConnectionManager()

class Note:
    def __init__(self, title, tags, content):
        self.title = title
        self.tags = tags
        self.content = content

class NotesBook:
    def __init__(self):
        self.data_repo = DataRepository(db_manager)

    def input(self, title, tags, content):
        note = Note(title, tags, content)
        return note

    def create(self, note):
        self.data_repo.create(note)
        print("Note created successfully.")


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
