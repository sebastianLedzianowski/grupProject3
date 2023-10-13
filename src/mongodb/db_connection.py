from pymongo import MongoClient
from dotenv import load_dotenv
import os


class DatabaseConnectionManager:
    """
    A class used to manage connections and operations with the MongoDB database.

    ...

    Attributes
    ----------
    url : str
        The URL of the MongoDB instance.
    client : MongoClient
        The client used to interact with the MongoDB instance.
    db : Database
        The database instance used to interact with collections.
    address_book : Collection
        A collection in the database used to store address book entries.
    note_book : Collection
        A collection in the database used to store notebook entries.

    """
    def __init__(self):
        load_dotenv()
        self.url = os.getenv("DB_URL")
        self.client = MongoClient(self.url)
        self.db = self.client['db_project3']
        self.address_book = self.db["address_book"]
        self.note_book = self.db["note_book"]
