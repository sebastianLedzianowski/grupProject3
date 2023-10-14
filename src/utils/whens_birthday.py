from src.mongodb.db_connection import DatabaseConnectionManager
from src.mongodb.db_repository import DataRepository
from src.mongodb.models import AddressBook
from datetime import datetime

db_manager = DatabaseConnectionManager()
data_repo = DataRepository(db_manager)


# stwórz funkcje ktora pobiera dane z książki kontaktów.
#
# sortuj kontakty po dacie urodzenia
#
# wyświetl kto dnia dzisiejszego urodziny oraz kto w najbliższych dniach
# (30 dni) będzie je obchodził  oraz które to będą urodziny.



# fukcnaj ktaora pobiera informacje kto dni dzisijejdszego ma urodziny i generuje dla tej osoby rzyczenia urodzinowe.