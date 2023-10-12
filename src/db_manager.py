from pymongo import MongoClient
from dotenv import load_dotenv
import os


class DatabaseManager:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv("DB_URL")
        self.client = MongoClient(self.url)
        self.db = self.client['mydatabase']
        self.customers = self.db["customers"]

    def show_all(self):
        for i in self.customers.find():
            print(i)


db = DatabaseManager().show_all()

