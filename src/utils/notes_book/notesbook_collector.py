from dataclasses import asdict
from src.mongodb.models import NoteBook
from src.utils.data_decorators import validate_input


class NotesBookCollector:
    @staticmethod
    @validate_input("Enter Title:")
    def get_title():
        pass

    @staticmethod
    @validate_input("Enter Tag:")
    def get_tag():
        pass


    @staticmethod
    @validate_input("Enter Content:")
    def get_content():
        pass

    @staticmethod
    def get_user_input():
        title = NotesBookCollector.get_title()
        tag = [NotesBookCollector.get_tag()]
        content = NotesBookCollector.get_content()

        notes_book_entry = NoteBook(
            title=title,
            tag=tag,
            content=content
        )

        return asdict(notes_book_entry)