from src.utils.contact_book.contact_book_manager import ContactBookManager
from mongomock import MongoClient
import pytest


# Mock the database connection for testing
@pytest.fixture
def mock_db_manager(monkeypatch):
    def mock_mongo_client(*args, **kwargs):
        return MongoClient()

    monkeypatch.setattr('pymongo.MongoClient', mock_mongo_client)


@pytest.fixture
def contact_manager(mock_db_manager):
    return ContactBookManager()


def test_create_contact(contact_manager):
    user_data = {
        'name': 'Test',
        'surname': 'Tester',
        'phone_number': '123456789',
        'email': 'test.tester@example.com',
        'birthday': '1990-01-01'
    }
    contact_manager.create(user_data)
    contacts = contact_manager.read_all()
    assert len(contacts) >= 1
    names = [contact['name'] for contact in contacts]
    assert 'Test' in names


def test_edit_contact(contact_manager):
    updates = {'name': 'Testera'}
    contact_manager.edit(field='name', value='Test', updates=updates)
    contacts = contact_manager.read_all()
    assert len(contacts) >= 1
    names = [contact['name'] for contact in contacts]
    assert 'Testera' in names


def test_delete_contact(contact_manager):
    contact_manager.delete(field='name', value='Testera')
    contacts = contact_manager.read_all()
    names = [contact['name'] for contact in contacts]
    assert 'Testera' not in names
