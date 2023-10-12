from dataclasses import dataclass
from typing import List


@dataclass
class AdressBook:
    imie: str
    nazwisko: str
    numer_telefonu: str
    email: str
    data_urodzin: str


@dataclass
class NoteBook:
    tytul: str
    tresc: str
    tagi: List[str]
