from datetime import datetime


def get_days_to_birthday(self):
    today = datetime.now()
    contacts = self.data_repo.contacts
    sorted_contacts_by_birthday = sorted(contacts, key=lambda x: x.birthday)

    birthday = datetime.strptime(self.birthday, "%d %B %Y")
    today_birthday = []
    upcoming_birthdays = []

    for contact in sorted_contacts_by_birthday:
        next_birthday = datetime(today.year, contact.birthday.month, contact.birthday.day)
        days_until_birthday = (next_birthday - today).days

        if days_until_birthday == 0:
            today_birthday.append(contact(contact.surname, contact.name))
        elif 0 < days_until_birthday <= 30:
            upcoming_birthdays.append(contact(contact.surname, contact.name))

    if today_birthday:
        today_birthday_msg = f"Today {self.user_data.name} {self.user_data.surname} has {today.year-birthday.year} birthday!\n"

    upcoming_birthday_msg = ""
    for contact, days_until_birthday in upcoming_birthdays:
        upcoming_birthday_msg += f"{contact.name} {contact.surname} will have {today.year-birthday.year} birthday."

    return self.today_birthday_msg + upcoming_birthday_msg

