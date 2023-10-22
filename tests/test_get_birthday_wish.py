from src.utils.contact_book.contact_book_manager import ContactBookManager
from bson import ObjectId
from mongomock import MongoClient
import pytest


# Mock the database connection for testing
@pytest.fixture
def mock_db_manager(monkeypatch):
    def mock_mongo_client(*args, **kwargs):
        return MongoClient()

    monkeypatch.setattr('pymongo.MongoClient', mock_mongo_client)


@pytest.fixture
def contact_manager(mock_db_manager, request):
    manager = ContactBookManager()
    inserted_ids = []

    def delete_inserted_docs():
        for _id in inserted_ids:
            manager.delete(field='_id', value=ObjectId(_id))

    request.addfinalizer(delete_inserted_docs)
    return manager, inserted_ids
def test_get_birthday_wish(contact_manager):
    name = 'Test'
    response = ContactBookManager().get_birthday_wish(name)
    json_data = response.json()
    assert name in json_data['wish']