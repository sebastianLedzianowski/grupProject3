from dataclasses import dataclass
from typing import List


@dataclass
class AddressBook:
    name: str
    surname: str
    phone_number: str
    email: str
    birthday: str


@dataclass
class NoteBook:
    title: str
    content: str
    tag: List[str]
