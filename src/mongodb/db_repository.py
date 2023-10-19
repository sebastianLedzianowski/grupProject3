from dataclasses import asdict
from typing import Type, List, Union
from src.mongodb.models import AddressBook, NoteBook


class DataRepository:
    def __init__(self, db_connection):
        """
        Initialize the data repository with a database manager.

        Args:
        - db_manager: An instance of a manager handling database connections.
        """
        self.db_connection = db_connection

    def _select_collection(self, value_type: Type[Union[AddressBook, NoteBook]]):
        """
        Select the appropriate database collection based on the data type.

        Args:
        - value_type (Type[Union[AddressBook, NoteBook]]): The type of the data model.

        Returns:
        - Collection: The selected database collection.

        Raises:
        - ValueError: If the provided data type doesn't match any collection.
        """
        if value_type == AddressBook:
            return self.db_connection.address_book
        elif value_type == NoteBook:
            return self.db_connection.note_book
        else:
            raise ValueError('No such database collection for given type.')

    def create(self, value_type: Union[AddressBook, NoteBook]):
        """
        Create a new entry in the database.

        Args:
        - value_type (Union[AddressBook, NoteBook]): Instance of the data model to be added to the database.

        Returns:
        - ObjectId: The ID of the inserted database entry.
        """
        collection = self._select_collection(type(value_type))
        return collection.insert_one(asdict(value_type)).inserted_id

    def read_all(self, value_type: Type[Union[AddressBook, NoteBook]]) -> List[Union[AddressBook, NoteBook]]:
        """
        Retrieve all entries from a collection in the database.

        Args:
        - value_type (Type[Union[AddressBook, NoteBook]]): The type of the data model to determine the collection.

        Returns:
        - List[Union[AddressBook, NoteBook]]: A list of all entries in the collection.
        """
        collection = self._select_collection(value_type)
        return [i for i in collection.find()]

    def update(self, value_type: Type[Union[AddressBook, NoteBook]], field: str, value: str, updates: dict):
        """
        Update an entry in the database.

        Args:
        - value_type (Type[Union[AddressBook, NoteBook]]): The type of the data model to determine the collection.
        - field (str): The name of the field to be used as a query.
        - value (str): The value to match against the query field.
        - updates (dict): A dictionary containing the update operators or document.

        Returns:
        - UpdateResult: The result of the update operation.
        """
        collection = self._select_collection(value_type)
        return collection.update_one({field: value}, {'$set': updates})
    

    def update_by_criteria(self, value_type: Type[Union[AddressBook, NoteBook]], search_criteria: dict, updates: dict):
        collection = self._select_collection(value_type)
        return collection.update_one(search_criteria, {'$set': updates})



    def delete(self, value_type: Type[Union[AddressBook, NoteBook]], field: str, value: str):
        """
        Delete an entry from the database.

        Args:
        - value_type (Type[Union[AddressBook, NoteBook]]): The type of the data model to determine the collection.
        - field (str): The name of the field to be used as a query.
        - value (str): The value to match against the query field.

        Returns:
        - DeleteResult: The result of the delete operation.
        """
        collection = self._select_collection(value_type)
        return collection.delete_one({field: value})

