import requests

from src.utils.contact_book.contact_book_manager import ContactBookManager


def test_get_birthday_wish(name):
    try:
        response = ContactBookManager().get_birthday_wish(name)
    except requests.RequestException as e:
        print(f"An error occurred while making the HTTP request: {str(e)}")
        return []

    try:
        json_data = response.json()
        print("JSON Data:", json_data)
    except ValueError as e:
        print(f"An error occurred while decoding JSON: {str(e)}")
        return []


test_get_birthday_wish('Barbara')
