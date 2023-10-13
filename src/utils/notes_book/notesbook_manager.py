from src.mongodb.db_connection import DatabaseConnectionManager
from src.mongodb.db_repository import DataRepository



class NotesBook:
    def __init__(self):
        self.db_manager = DatabaseConnectionManager()
        self.data_repo = DataRepository(self.db_manager)

    def create(self, note):
        pass


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
