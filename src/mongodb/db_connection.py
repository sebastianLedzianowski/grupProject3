from pymongo import MongoClient
from dotenv import load_dotenv
import os


class DatabaseConnectionManager:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv("DB_URL")
        self.client = MongoClient(self.url)
        self.db = self.client['db_project3']
        self.address_book = self.db["address_book"]
        self.note_book = self.db["note_book"]
