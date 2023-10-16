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

    def read_all(self):
        try:
            all_documents = self.data_repo.read_all(NoteBook)
            return list(all_documents)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return []

    def sorted(self, sort_key) -> list:
        try:
            notes = self.data_repo.read_all(NoteBook)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return []

        sorted_notes = sorted(notes, key=lambda x: x.get(sort_key))

        return sorted_notes

    def edit(self, field, value, new_value):
        try:
            self.data_repo.update(value_type=NoteBook, field=field, value=value, new_value=new_value)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    
    def delete(self, field, value):
        try:
            self.data_repo.delete(value_type=NoteBook, field=field, value=value)
        except Exception as e:
            print(f"An error occurred: {str(e)}")    
