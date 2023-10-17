from src.utils.contact_book.contact_book_manager import ContactBookManager
from datetime import date, timedelta


def test_get_days_to_birthday():
    cbm = ContactBookManager()
    today = date(2023, 10, 16)
    today_to_30 = today + timedelta(days=30)
    upcoming_birthdays = cbm.get_days_to_birthday()

    for info in upcoming_birthdays:
        name = info["name"]
        birthday = info["birthday"]
        days_to_birthday = info["days_to_birthday"]
        print(f"{name} ma urodziny {birthday} za {days_to_birthday} dni.")

if __name__ == '__main__':
    test_get_days_to_birthday()
