# MongoDB Module Documentation

---

## [models.py](https://github.com/sebastianLedzianowski/grupProject3/blob/main/src/mongodb/models.py)

This file contains data models for the application.

### Classes:

- `AddressBook`: Represents an entry in a contact book.
- `NoteBook`: Represents a note entry.

### Example Usage:

```python
from src.mongodb.models import AddressBook, NoteBook

# Creating an AddressBook entry
address_entry = AddressBook(
    name="John",
    surname="Doe",
    phone_number="123456789",
    email="john@example.com",
    birthday="2000-01-01"
)

# Creating a NoteBook entry
note_entry = NoteBook(
    title="Meeting Notes",
    content="Discussed project milestones and deadlines.",
    tag=["meeting", "project"]
)
```
## [db_connection.py](https://github.com/sebastianLedzianowski/grupProject3/blob/main/src/mongodb/db_connection.py)

This file manages connections and operations with the MongoDB database.

- `DatabaseConnectionManager`: Manages connections and operations with the MongoDB database.

### Example Usage:

```python
from src.mongodb.db_connection import DatabaseConnectionManager

# Creating a DatabaseConnectionManager instance
db_connection = DatabaseConnectionManager()

# Accessing a collection
address_book_collection = db_connection.address_book
note_book_collection = db_connection.note_book
```

## [db_repository.py](https://github.com/sebastianLedzianowski/grupProject3/blob/main/src/mongodb/db_repository.py)

This file provides a class for interacting with the database.

### Class

- `DataRepository`: Provides methods to interact with the MongoDB database, performing basic CRUD operations.

### Example Usage:

```python
from src.mongodb.db_repository import DataRepository
from src.mongodb.db_connection import DatabaseConnectionManager
from src.mongodb.models import AddressBook

# Initialize the database connection and repository
db_manager = DatabaseConnectionManager()
data_repo = DataRepository(db_manager)

# Example data
address_data = {
    'name': 'John',
    'surname': 'Doe',
    'phone_number': '123456789',
    'email': 'john@example.com',
    'birthday': '2000-01-01'
}

# Create a new entry
address_entry = AddressBook(**address_data)
data_repo.create(address_entry)

# Read all entries
all_addresses = data_repo.read_all(AddressBook)

# Update an entry
data_repo.update(
    value_type=AddressBook,
    field='name',
    value='John',
    updates={'name': 'Jonathan'}
)

# Delete an entry
data_repo.delete(
    value_type=AddressBook,
    field='name',
    value='Jonathan'
)
```

## Methods

- `create(self, value_type: Union[AddressBook, NoteBook]) -> ObjectId`:
  - Description: Adds a new entry to the database.
  - Parameters:
    - `value_type`: An instance of the data model to be added to the database.
  - Returns: The ID of the inserted database entry.
- `read_all(self, value_type: Type[Union[AddressBook, NoteBook]]) -> List[Union[AddressBook, NoteBook]]`
  - Description: Retrieves all entries from a collection in the database.
  - Parameters:
    - `value_type`: The type of the data model to determine the collection.
  - Returns: A list of all entries in the collection.
- `update(self, value_type: Type[Union[AddressBook, NoteBook]], field: str, value: str, updates: dict) -> UpdateResult`
  - Description: Updates an entry in the database.
  - Parameters:
    - `value_type`: The type of the data model to determine the collection.
    - `field`: The name of the field to be used as a query.
    - `value`: The value to match against the query field.
    - `updates`: A dictionary containing the update operators or document.
  - Returns: The result of the update operation.
- `delete(self, value_type: Type[Union[AddressBook, NoteBook]], field: str, value: str) -> DeleteResult`:
  - Description: Deletes an entry from the database.
  - Parameters:
    - `value_type`: The type of the data model to determine the collection.
    - `field`: The name of the field to be used as a query.
    - `value`: The value to match against the query field.
  Returns: The result of the delete operation.

---

Note: Ensure to install the necessary packages and set up the environment variables for database connection.

---




