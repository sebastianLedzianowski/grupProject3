from src.utils.contact_book.contact_book_manager import ContactBookManager
from src.utils.notes_book.notesbook_manager import NotesBookManager
from src.utils.contact_book.contact_book_collector import ContactBookCollector
from src.utils.notes_book.notesbook_collector import NotesBookCollector
# import os
# import smtplib
# from email.message import EmailMessage
# import ssl
# from dotenv import load_dotenv

from src.utils.send_email import send_email


def main():
    contact_book_manager = ContactBookManager()
    notes_book_manager = NotesBookManager()
    while True:
        print("\n===== Main Menu =====")
        print("1. Manage Contacts")
        print("2. Manage Notes")
        print("3. Check Days Until Next Birthday")
        print("4. Exit Program")
        try:
            choice = int(input("Choose option (1/2/3/4): "))
        except ValueError:
            print("Error! Enter a number.")
            continue
        if choice == 1:
            contact_menu(contact_book_manager)
        elif choice == 2:
            notes_menu(notes_book_manager)
        elif choice == 3:
            check_birthday_menu(contact_book_manager)
        elif choice == 4:
            print("Closing the program. Goodbye!")
            break

        else:
            print("Invalid choice. Choose an option from 1 to 3.")


def contact_menu(contact_book_manager):
    while True:
        print("\n===== Manage Contacts =====")
        print("1. Display Contacts")
        print("2. Add Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Sort Contacts")
        print("6. Back to Main Menu")
        try:
            contact_choice = int(input("Choose option (1/2/3/4/5/6): "))
        except ValueError:
            print("Error! Enter a number.")
            continue
        if contact_choice == 1:
            contacts = contact_book_manager.read_all()
            if not contacts:
                print("No contacts found.")
            else:
                max_name_length = max(len(contact.get('name', '')) for contact in contacts)
                max_surname_length = max(len(contact.get('surname', '')) for contact in contacts)
                max_phone_number_length = max(len(contact.get('phone_number', '')) for contact in contacts)
                max_email_length = max(len(contact.get('email', '')) for contact in contacts)
                max_birthday_length = max(len(contact.get('birthday', '')) for contact in contacts)
                print("\n| {:^{}} | {:^{}} | {:^{}} | {:^{}} | {:^{}} |".format('Name', max_name_length, 'Surname',
                                                                                max_surname_length, 'Phone number',
                                                                                max_phone_number_length, 'Email',
                                                                                max_email_length, 'Birthday',
                                                                                max_birthday_length))
                separator_line = "|{}+{}+{}+{}+{}|".format("-" * (max_name_length + 2), "-" * (max_surname_length + 2),
                                                           "-" * (max_phone_number_length + 2), "-" * (max_email_length
                                                                                                       + 2),
                                                           "-" * (max_birthday_length + 2))
                print(separator_line)
                for contact in contacts:
                    name = contact.get('name', '')[:max_name_length]
                    surname = contact.get('surname', '')[:max_surname_length]
                    phone_number = contact.get('phone_number', '')[:max_phone_number_length]
                    email = contact.get('email', '')[:max_email_length]
                    birthday = contact.get('birthday', '')[:max_birthday_length]
                    print("| {:^{}} | {:^{}} | {:^{}} | {:^{}} | {:^{}} |".format(name, max_name_length, surname,
                                                                                  max_surname_length, phone_number,
                                                                                  max_phone_number_length, email,
                                                                                  max_email_length, birthday,
                                                                                  max_birthday_length))
                    print(separator_line)
        elif contact_choice == 2:
            user_data = ContactBookCollector.get_user_input()
            contact_book_manager.create(user_data)
            print("Contact added successfully.")
        elif contact_choice == 3:
            print("\n===== Edit Contact =====")
            print("1. Edit by Name")
            print("2. Edit by Surname")
            print("3. Edit by Phone number")
            print("4. Edit by Email")
            print("5. Edit by Birthday")
            print("6. Back to Manage Contacts")
            try:
                edit_choice = int(input("Choose edit option (1/2/3/4/5/6): "))
            except ValueError:
                print("Error! Enter a number.")
                continue
            if edit_choice in range(1, 6):
                fields = ["name", "surname", "phone number", "email", "birthday"]
                field = fields[edit_choice - 1]
                value = input(f"Enter the current value of the {field}: ")
                updates = input(f"Enter the new value for the {field}: ")
                contact_book_manager.edit(field, value, {field: updates})
            elif edit_choice == 6:
                print("Back to Manage Contacts.")
            else:
                print("Invalid choice. Choose an option from 1 to 6.")
        elif contact_choice == 4:
            print("\n===== Delete Contact =====")
            print("1. Delete by Name")
            print("2. Delete by Surname")
            print("3. Delete by Phone number")
            print("4. Delete by Email")
            print("5. Delete by Birthday")
            print("6. Back to Manage Contacts")
            try:
                delete_choice = int(input("Choose delete option (1/2/3/4/5/6): "))
            except ValueError:
                print("Error! Enter a number.")
                continue
            if delete_choice in range(1, 6):
                fields = ["name", "surname", "phone number", "email", "birthday"]
                field = fields[delete_choice - 1]
                value = input(f"Enter the value of the {field} to delete: ")
                contact_book_manager.delete(field, value)
            elif delete_choice == 6:
                print("Back to Manage Contacts.")
            else:
                print("Invalid choice. Choose an option from 1 to 6.")
        elif contact_choice == 5:
            print("\n===== Sort Contacts =====")
            print("1. Sort by Name")
            print("2. Sort by Surname")
            print("3. Sort by Phone number")
            print("4. Sort by Email")
            print("5. Sort by Birthday")
            print("6. Back to Manage Contacts")
            try:
                sort_choice = int(input("Choose sort option (1/2/3/4/5/6): "))
            except ValueError:
                print("Error! Enter a number.")
                continue
            if sort_choice in range(1, 6):
                fields = ["name", "surname", "phone number", "email", "birthday"]
                sort_key = fields[sort_choice - 1]
                sorted_contacts = contact_book_manager.get_sorted_contacts(sort_key)
                if not sorted_contacts:
                    print("No contacts found.")
                else:
                    max_name_length = max(len(contact.get('name', '')) for contact in sorted_contacts)
                    max_surname_length = max(len(contact.get('surname', '')) for contact in sorted_contacts)
                    max_phone_number_length = max(len(contact.get('phone_number', '')) for contact in sorted_contacts)
                    max_email_length = max(len(contact.get('email', '')) for contact in sorted_contacts)
                    max_birthday_length = max(len(contact.get('birthday', '')) for contact in sorted_contacts)
                    print(f"\nSorted Contacts by: {sort_key} ")
                    print("| {:^{}} | {:^{}} | {:^{}} | {:^{}} | {:^{}} |".format('Name', max_name_length, 'Surname',
                                                                                  max_surname_length, 'Phone number',
                                                                                  max_phone_number_length, 'Email',
                                                                                  max_email_length, 'Birthday',
                                                                                  max_birthday_length))
                    separator_line = "|{}+{}+{}+{}+{}|".format("-" * (max_name_length + 2),
                                                               "-" * (max_surname_length + 2),
                                                               "-" * (max_phone_number_length + 2),
                                                               "-" * (max_email_length + 2),
                                                               "-" * (max_birthday_length + 2))
                    print(separator_line)
                    for contact in sorted_contacts:
                        name = contact.get('name', '')[:max_name_length]
                        surname = contact.get('surname', '')[:max_surname_length]
                        phone_number = contact.get('phone_number', '')[:max_phone_number_length]
                        email = contact.get('email', '')[:max_email_length]
                        birthday = contact.get('birthday', '')[:max_birthday_length]
                        print("| {:^{}} | {:^{}} | {:^{}} | {:^{}} | {:^{}} |".format(name, max_name_length, surname,
                                                                                      max_surname_length, phone_number,
                                                                                      max_phone_number_length, email,
                                                                                      max_email_length, birthday,
                                                                                      max_birthday_length))
                        print(separator_line)
            elif sort_choice == 6:
                print("Back to Manage Contacts.")
            else:
                print("Invalid choice. Choose an option from 1 to 6.")
        elif contact_choice == 6:
            print("Back to Main Menu.")
            break
        else:
            print("Invalid choice. Choose an option from 1 to 6.")


def notes_menu(notes_book_manager):
    while True:
        print("\n===== Manage Notes =====")
        print("1. Display Notes")
        print("2. Add Note")
        print("3. Edit Note")
        print("4. Delete Note")
        print("5. Sort Notes")
        print("6. Back to Main Menu")
        try:
            notes_choice = int(input("Choose option (1/2/3/4/5/6): "))
        except ValueError:
            print("Error! Enter a number.")
            continue
        if notes_choice == 1:
            notes = notes_book_manager.read_all()
            note_number = 1
            if not notes:
                print("No notes found.")
            else:
                for note in notes:
                    title = note.get("title", "")
                    tags = ", ".join(note.get("tag", []))
                    content = note.get("content", "")
                    print(f'\nNote Number: {note_number}')
                    print(f'Title: {title}')
                    print(f'Tags: {tags}')
                    print(f'Content: {content}')
                    note_number += 1
        elif notes_choice == 2:
            user_data = NotesBookCollector.get_user_input()
            notes_book_manager.create(user_data)
        elif notes_choice == 3:
            print("\n===== Edit Note =====")
            print("1. Edit by Title")
            print("2. Edit by Tag")
            print("3. Edit by Content")
            print("4. Back to Manage Notes")
            try:
                edit_choice = int(input("Choose edit option (1/2/3/4): "))
            except ValueError:
                print("Error! Enter a number.")
                continue
            if edit_choice in range(1, 4):
                fields = ["title", "tag", "content"]
                field = fields[edit_choice - 1]
                value = input(f"Enter the current value of the {field}: ")
                updates = input(f"Enter the new value for the {field}: ")
                notes_book_manager.edit(field, value, {field: updates})
            elif edit_choice == 4:
                print("Back to Manage Notes.")

            else:
                print("Invalid choice. Choose an option from 1 to 4.")
        elif notes_choice == 4:
            print("\n===== Delete Note =====")
            print("1. Delete by Title")
            print("2. Delete by Tag")
            print("3. Delete by Content")
            print("4. Back to Manage Notes")
            try:
                delete_choice = int(input("Choose delete option (1/2/3/4): "))
            except ValueError:
                print("Error! Enter a number.")
                continue
            if delete_choice in range(1, 4):
                fields = ["title", "tag", "content"]
                field = fields[delete_choice - 1]
                value = input(f"Enter the value of the {field} to delete: ")
                notes_book_manager.delete(field, value)
            elif delete_choice == 4:
                print("Back to Manage Notes.")
            else:
                print("Invalid choice. Choose an option from 1 to 4.")
        elif notes_choice == 5:
            print("\n===== Sort Notes =====")
            print("1. Sort by Title")
            print("2. Sort by Tag")
            print("3. Sort by Content")
            print("4. Back to Manage Notes")
            try:
                sort_choice = int(input("Choose sort option (1/2/3/4): "))
            except ValueError:
                print("Error! Enter a number.")
                continue
            if sort_choice in range(1, 4):
                fields = ["title", "tag", "content"]
                sort_key = fields[sort_choice - 1]
                sorted_notes = notes_book_manager.sorted(sort_key)
                note_number = 1
                if not sorted_notes:
                    print("No notes found.")
                else:
                    for note in sorted_notes:
                        title = note.get("title", "")
                        tags = ", ".join(note.get("tag", []))
                        content = note.get("content", "")
                        print(f'\nNote Number: {note_number}')
                        print(f'Title: {title}')
                        print(f'Tags: {tags}')
                        print(f'Content: {content}')
                        note_number += 1
            elif sort_choice == 4:
                print("Back to Manage Notes.")
            else:
                print("Invalid choice. Choose an option from 1 to 4.")
        elif notes_choice == 6:
            print("Back to Main Menu.")
            break
        else:
            print("Invalid choice. Choose an option from 1 to 6.")


def check_birthday_menu(contact_book_manager):
    while True:
        upcoming_birthdays = contact_book_manager.get_days_to_birthday()
        print("\n======== Check Days Until Next Birthday ========")
        if not upcoming_birthdays:
            print("No upcoming birthdays found.")
        else:
            for birthday_info in upcoming_birthdays:
                print(
                    f"{birthday_info['name']} {birthday_info['surname']}'s birthday is in "
                    f"{birthday_info['days_to_birthday']} days.")
                if birthday_info['days_to_birthday'] == 0:
                    email = birthday_info['email']
                    generate_birthday_wish(contact_book_manager, birthday_info, email)


def generate_birthday_wish(contact_book_manager, name, email):
    while True:
        print(f"Would you like to generate birthday wishes {name['name']}?")
        print("1. Yes")
        print("2. No")
        user_choice = int(input("Choose option (1/2): "))
        if user_choice == 1:
            response = contact_book_manager.get_birthday_wish(name)
            if response and response.status_code == 200:
                wish = response.json()['wish']
                print("Birthday wishes generated successfully:")
                print(f'{wish}')
                return handle_send_email(name, email, wish)
            else:
                print("Error generating birthday wishes.")
        elif user_choice == 2:
            print("Birthday wishes not generated.")
            return main()
        else:
            print("Invalid choice. Birthday wishes not generated.")


def handle_send_email(name, email, wish):
    while True:
        print(f"\nDo you want to send an email with birthday wishes {name['name']}?")
        print("1. Yes")
        print("2. No")
        user_choice = int(input("Choose option (1/2):\n "))
        if user_choice == 1:
            return send_email(email, "Birthday Wishes", wish)
        print("Invalid input. Please enter a number.\n")


if __name__ == '__main__':
    main()
