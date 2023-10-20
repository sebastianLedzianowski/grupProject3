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


def test_create_contact(contact_manager):
    manager, inserted_ids = contact_manager
    user_data = {
        'name': 'CreateTest',
        'surname': 'Creator',
        'phone_number': '987654321',
        'email': 'create.test@example.com',
        'birthday': '1991-05-15'
    }

    try:
        manager.create(user_data)
        contacts = manager.read_all()
        assert len(contacts) != 0
        names = [contact['name'] for contact in contacts]
        assert user_data['name'] in names

    finally:
        # Append the _id of the created contact to inserted_ids for cleanup
        for contact in contacts:
            if contact['name'] == user_data['name']:
                inserted_ids.append(contact['_id'])


def test_read_all(contact_manager):
    manager, inserted_ids = contact_manager
    user_data = {
        'name': 'ReadTest',
        'surname': 'Reader',
        'phone_number': '987654321',
        'email': 'read.test@example.com',
        'birthday': '1995-05-15'
    }
    manager.create(user_data)

    try:
        # Fetch all contacts
        contacts = manager.read_all()
        # Check if the newly created contact exists in the fetched contacts
        names = [contact['name'] for contact in contacts]
        assert user_data['name'] in names

    finally:
        # Append the _id of the created contact to inserted_ids for cleanup
        for contact in contacts:
            if contact['name'] == user_data['name']:
                inserted_ids.append(contact['_id'])


def test_edit_contact(contact_manager):
    manager, inserted_ids = contact_manager

    # Create a new contact for the test
    user_data = {
        'name': 'EditTest',
        'surname': 'Editor',
        'phone_number': '987123456',
        'email': 'edit.test@example.com',
        'birthday': '1992-04-14'
    }
    manager.create(user_data)
    try:
        # Edit the newly created contact
        new_name = 'EditedName'
        manager.edit(field='name', value=user_data['name'], updates={'name': new_name})

        # Fetch all contacts
        contacts = manager.read_all()

        # Check if the contact was edited correctly
        names = [contact['name'] for contact in contacts]
        assert new_name in names

    finally:
        # Append the _id of the edited contact to inserted_ids for cleanup
        for contact in contacts:
            if contact['name'] == new_name:
                inserted_ids.append(contact['_id'])


def test_get_sorted_contacts(contact_manager):
    manager, inserted_ids = contact_manager

    # Create a couple of new contacts for the test
    user_data1 = {
        'name': 'Zzzzeta',
        'surname': 'Zetor',
        'phone_number': '987123456',
        'email': 'zeta.zetor@example.com',
        'birthday': '1992-04-14'
    }
    manager.create(user_data1)

    user_data2 = {
        'name': '',
        'surname': 'Alphor',
        'phone_number': '123456789',
        'email': 'alpha.alphor@example.com',
        'birthday': '1990-01-01'
    }
    manager.create(user_data2)

    try:
        # Fetch and sort contacts by name
        sorted_contacts = manager.get_sorted_contacts('name')

        # Check if the contacts are sorted correctly
        assert sorted_contacts[0]['name'] == user_data2['name']
        assert sorted_contacts[-1]['name'] == user_data1['name']

    finally:
        # Append the _ids of the created contacts to inserted_ids for cleanup
        contacts = manager.read_all()
        for contact in contacts:
            if contact['name'] in [user_data1['name'], user_data2['name']]:
                inserted_ids.append(contact['_id'])


def test_delete_contact(contact_manager):
    manager, inserted_ids = contact_manager

    # Create a new contact for the test
    user_data = {
        'name': 'DeleteTest',
        'surname': 'Deletor',
        'phone_number': '456789123',
        'email': 'delete.test@example.com',
        'birthday': '1994-06-16'
    }
    manager.create(user_data)

    # Delete the newly created contact
    manager.delete(field='name', value=user_data['name'])

    # Fetch all contacts
    contacts = manager.read_all()

    # Check if the contact was deleted correctly
    names = [contact['name'] for contact in contacts]
    assert user_data['name'] not in names


def test_get_birthday_wish(contact_manager):
    name = 'Test'
    response = ContactBookManager().get_birthday_wish(name)
    json_data = response.json()
    assert name in json_data['wish']


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
