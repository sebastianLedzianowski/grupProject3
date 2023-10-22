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

def test_get_days_to_birthday(contact_manager):
    from datetime import date, timedelta
    manager, inserted_ids = contact_manager
    birthday_today = date.today()
    birthday_soon = birthday_today + timedelta(days=2)
    birthday_after_30_days = birthday_today + timedelta(days=31)

    # Create a couple of new contacts for the test
    user_data1 = {
        'name': 'BirthdaySoon',
        'surname': 'Soonson',
        'phone_number': '987654321',
        'email': 'soon@example.com',
        'birthday': f'{birthday_soon.year}-{birthday_soon.month}-{birthday_soon.day}'
    }
    manager.create(user_data1)

    user_data2 = {
        'name': 'BirthdayToday',
        'surname': 'Todayson',
        'phone_number': '123456789',
        'email': 'today@example.com',
        'birthday': f'{birthday_today.year}-{birthday_today.month}-{birthday_today.day}'
    }
    manager.create(user_data2)

    user_data3 = {
        'name': 'BirthdayAfter30',
        'surname': 'After',
        'phone_number': '123456789',
        'email': 'after@example.com',
        'birthday': f'{birthday_after_30_days.year}-{birthday_after_30_days.month}-{birthday_after_30_days.day}'
    }

    manager.create(user_data3)

    try:
        upcoming_birthdays = manager.get_days_to_birthday

        # Check if the birthdays are fetched correctly
        assert any(contact['name'] == user_data1['name'] and contact['days_to_birthday'] == 2 for contact in
                   upcoming_birthdays), f"Expected 2 days to birthday for {user_data1['name']}," \
                                        f" but got a different value."
        assert any(contact['name'] == user_data2['name'] and contact['days_to_birthday'] == 0 for contact in
                   upcoming_birthdays), f"Expected 0 days to birthday for {user_data2['name']}," \
                                        f" but got a different value."
        assert not any(contact['name'] == user_data3['name'] for contact in
                       upcoming_birthdays), f"{user_data3['name']}'s " \
                                            f"birthday should not be in the upcoming birthdays list."
    finally:
        # Append the _ids of the created contacts to inserted_ids for cleanup
        contacts = manager.read_all()
        for contact in contacts:
            if contact['name'] in [user_data1['name'], user_data2['name'], user_data3['name']]:
                inserted_ids.append(contact['_id'])