from src.utils.notes_book.notesbook_manager import NotesBookManager
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
def notes_manager(mock_db_manager, request):
    manager = NotesBookManager()
    inserted_ids = []

    def delete_inserted_docs():
        for _id in inserted_ids:
            manager.delete(field='_id', value=ObjectId(_id))

    request.addfinalizer(delete_inserted_docs)
    return manager, inserted_ids


def test_create_note(notes_manager):
    manager, inserted_ids = notes_manager
    user_data = {
        'title': 'CreateTest',
        'tag': ['Create_Tag1, Create_Tag2'],
        'content': 'CreateContent'
    }

    try:
        manager.create(user_data)
        notes = manager.read_all()
        assert len(notes) != 0
        titles = [note['title'] for note in notes]
        assert user_data['title'] in titles

    finally:
        # Append the _id of the created contact to inserted_ids for cleanup
        for note in notes:
            if note['title'] == user_data['title']:
                inserted_ids.append(note['_id'])


def test_read_all(notes_manager):
    manager, inserted_ids = notes_manager
    user_data = {
        'title': 'ReadTest',
        'tag': ['Read_Tag1, Read_Tag2'],
        'content': 'ReadContent'
    }

    manager.create(user_data)
    notes = manager.read_all()
    try:
        titles = [note['title'] for note in notes]
        assert user_data['title'] in titles

    finally:
        # Append the _id of the created contact to inserted_ids for cleanup
        for note in notes:
            if note['title'] == user_data['title']:
                inserted_ids.append(note['_id'])


def test_edit_note(notes_manager):
    manager, inserted_ids = notes_manager

    # Create a new contact for the test
    user_data = {
        'title': 'EditTest',
        'tag': ['Edit_Tag1, Edit_Tag2'],
        'content': 'EditContent'
    }

    manager.create(user_data)
    try:
        # Edit the newly created contact
        new_title = 'EditedTitle'
        manager.edit(field='title', value=user_data['title'], updates={'title': new_title})

        # Fetch all contacts
        notes = manager.read_all()

        # Check if the contact was edited correctly
        titles = [note['title'] for note in notes]
        assert new_title in titles

    finally:
        # Append the _id of the edited contact to inserted_ids for cleanup
        for note in notes:
            if note['title'] == new_title:
                inserted_ids.append(note['_id'])


def test_delete_note(notes_manager):
    manager, inserted_ids = notes_manager

    # Create a new contact for the test
    user_data = {
        'title': 'DeleteTest',
        'tag': ['Delete_Tag1, Delete_Tag2'],
        'content': 'DeleteContent'
    }
    manager.create(user_data)

    # Delete the newly created contact
    manager.delete(field='title', value=user_data['title'])

    # Fetch all contacts
    notes = manager.read_all()

    # Check if the contact was deleted correctly
    titles = [note['title'] for note in notes]
    assert user_data['title'] not in titles

def test_sorted(notes_manager):
    manager, inserted_ids = notes_manager

    # Create a couple of new contacts for the test
    user_data1 = {
        'title': 'AaaaaTest',
        'tag': ['Sort_Tag1, Sort_Tag2'],
        'content': 'SortContent1'
    }
    manager.create(user_data1)

    user_data2 = {
        'title': 'ŻŻŻtest',
        'tag': ['Sort_Tag3, Sort_Tag4'],
        'content': 'SortContent2'
    }
    manager.create(user_data2)

    try:
        # Fetch and sort contacts by name
        sorted_notes = manager.sorted('title')

        # Check if the contacts are sorted correctly
        assert sorted_notes[0]['title'] == user_data1['title']
        assert sorted_notes[-1]['title'] == user_data2['title']

    finally:
        # Append the _ids of the created contacts to inserted_ids for cleanup
        notes = manager.read_all()
        for note in notes:
            if note['title'] in [user_data1['title'], user_data2['title']]:
                inserted_ids.append(note['_id'])
