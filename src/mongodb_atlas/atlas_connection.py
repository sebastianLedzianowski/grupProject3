import os

from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class DatabaseConnectionManager:

    def __init__(self):
        load_dotenv()
        self.uri = os.getenv("URI")
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        self.atlas = self.client['personal_assistant']
        self.contact_book = self.atlas['ContactBook']
        self.note_book = self.atlas['NoteBook']
