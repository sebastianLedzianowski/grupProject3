from src.mongodb.db_connection import DatabaseConnectionManager
from src.mongodb.db_repository import DataRepository
from src.mongodb.models import NoteBook

class NotesBookManager:
    def __init__(self):
        self.db_manager = DatabaseConnectionManager()
        self.data_repo = DataRepository(self.db_manager)

    def create(self, user_data):
        try:
            self.data_repo.create(NoteBook(title=user_data['title'],
                                              tag=user_data['tag'],
                                              content=user_data['content']))
        except Exception as e:
            print(f"An error occurred: {str(e)}")

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
