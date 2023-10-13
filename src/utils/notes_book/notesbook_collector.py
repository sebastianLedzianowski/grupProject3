from dataclasses import asdict
from src.mongodb.models import NoteBook

class NotesBookCollector:
    @staticmethod
    def get_user_input():
        title = input('Enter Title:')
        tag = [input('Enter Tag:')]
        content = input('Enter Content:')

        notes_book_entry = NoteBook(
            title=title,
            tag=tag,
            content=content
        )

        return asdict(notes_book_entry)