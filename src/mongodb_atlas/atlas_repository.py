from dataclasses import asdict
from typing import Type, List, Union
from src.mongodb_atlas.models import ContactBook, NoteBook

class DataRepository:
    def __init__(self, atlas_connection):
        self.atlas_connection = atlas_connection

    def _select_collection(self, value_type: Type[Union[ContactBook, NoteBook]]):
        if value_type == ContactBook:
            return self.atlas_connection.contact_book
        elif value_type == NoteBook:
            return self.atlas_connection.note_book
        else:
            raise ValueError('No such database collection for given type.')

    def create(self, value_type: Union[ContactBook, NoteBook]):
        collection = self._select_collection(type(value_type))
        return collection.insert_one(asdict(value_type)).inserted_id

    def read_all(self, value_type: Type[Union[ContactBook, NoteBook]]) -> List[Union[ContactBook, NoteBook]]:
        collection = self._select_collection(value_type)
        return [i for i in collection.find()]

    def update(self, value_type: Type[Union[ContactBook, NoteBook]], field: str, value: str, updates: dict):
        collection = self._select_collection(value_type)
        return collection.update_one({field: value}, {'$set': updates})

    def update_by_criteria(self, value_type: Type[Union[ContactBook, NoteBook]], search_criteria: dict, updates: dict):
        collection = self._select_collection(value_type)
        return collection.update_one(search_criteria, {'$set': updates})

    def delete(self, value_type: Type[Union[ContactBook, NoteBook]], field: str, value: str):
        collection = self._select_collection(value_type)
        return collection.delete_one({field: value})