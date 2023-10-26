from src.utils.contact_book.contact_book_collector import ContactBookCollector


def contact_menu(contact_book_manager):
    while True:
        print("\n===== Manage Contacts =====")
        print("1. Display Contacts")
        print("2. Add Contact")
        print("3. Choose Contact to edit/delete")
        print("4. Sort Contacts")
        print("5. Back to Main Menu")
        contact_choice = str(input("Choose option (1/2/3/4/5/6): "))
        if contact_choice == '1':
            contacts = contact_book_manager.read_all()
            display_contacts(contacts)
        elif contact_choice == '2':
            user_data = ContactBookCollector.get_user_input()
            contact_book_manager.create(user_data)
            print("Contact added successfully.")
        elif contact_choice == '3':
            choose_contact(contact_book_manager)
        elif contact_choice == '4':
            print("\n===== Sort Contacts =====")
            print("1. Sort by Name")
            print("2. Sort by Surname")
            print("3. Sort by Phone number")
            print("4. Sort by Email")
            print("5. Sort by Birthday")
            print("6. Back to Manage Contacts")
            sort_choice = str(input("Choose sort option (1/2/3/4/5/6): "))
            if sort_choice.isdigit() and int(sort_choice) in range(1, 6):
                fields = ["name", "surname", "phone_number", "email", "birthday"]
                sort_key = fields[int(sort_choice) - 1]
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
            elif sort_choice == '6':
                print("Back to Manage Contacts.")
            else:
                print("Invalid choice. Choose an option from 1 to 6.")
        elif contact_choice == '5':
            print("Back to Main Menu.")
            break
        else:
            print("Invalid choice. Choose an option from 1 to 6.")


def display_contacts(contacts):
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
                                                   "-" * (max_phone_number_length + 2), "-" * (max_email_length + 2),
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


def choose_contact(contact_book_manager):
    while True:
        print("\n===== Choose Contact by =====")
        print("1. Choose by Name")
        print("2. Choose by Surname")
        print("3. Choose by Phone number")
        print("4. Choose by Email")
        print("5. Choose by Birthday")
        print("6. Back to Manage Contacts Menu")
        choice = str(input("Choose edit option (1/2/3/4/5/6): "))
        if choice.isdigit() and int(choice) in range(1, 6):
            fields = ["name", "surname", "phone_number", "email", "birthday"]
            field = fields[int(choice) - 1]
            value = input(f"Enter the current value of the {field}: ")
            value = value.capitalize()
            duplicates = contact_book_manager.look_for_doubles(field, value)

            if duplicates:
                if len(duplicates) == 1:
                    print(f"Found a single contact with {field} = {value}:")
                    display_numbered_contacts([duplicates[0]])
                    _id = duplicates[0]["_id"]
                    contact_edit_delete_menu(contact_book_manager, field, value, _id)
                else:
                    print(f"Duplicates found for {field} = {value}. Choose a duplicate to edit:")
                    display_numbered_contacts(duplicates)
                    chosen_duplicate = str(input("Choose the duplicate to edit (1/2/...): "))
                    chosen_duplicate_index = int(chosen_duplicate) - 1
                    if 0 <= int(chosen_duplicate_index) < len(duplicates):
                        _id = duplicates[int(chosen_duplicate_index)]["_id"]
                        contact_edit_delete_menu(contact_book_manager, field, value, _id)
                    else:
                        print("Invalid choice. No contact edited.")
            else:
                all_contacts = contact_book_manager.read_all()
                matching_contacts = [contact for contact in all_contacts if contact[field] == value]

                if not matching_contacts:
                    print(f"No contact found with {field} = {value}. Please choose a valid contact.")
                else:
                    print(f"Found a single contact with {field} = {value}:")
                    display_numbered_contacts(matching_contacts)
                    contact_edit_delete_menu(contact_book_manager, field, value)
            break
        elif choice == '6':
            print("Back to Choose Contact Menu.")
            break
        else:
            print("Invalid choice. Choose an option from 1 to 6.")


def display_numbered_contacts(contacts):
    max_name_length = max(len(contact.get('name', '')) for contact in contacts)
    max_surname_length = max(len(contact.get('surname', '')) for contact in contacts)
    max_phone_number_length = max(len(contact.get('phone_number', '')) for contact in contacts)
    max_email_length = max(len(contact.get('email', '')) for contact in contacts)
    max_birthday_length = max(len(contact.get('birthday', '')) for contact in contacts)

    print("\n| {:^5} | {:^{}} | {:^{}} | {:^{}} | {:^{}} | {:^{}} |".format(
        'Index', 'Name', max_name_length, 'Surname', max_surname_length, 'Phone number',
        max_phone_number_length, 'Email', max_email_length, 'Birthday', max_birthday_length))

    separator_line = "|{:^7}|{}+{}+{}+{}+{}|".format(
        ' ', "-" * (max_name_length + 2), "-" * (max_surname_length + 2),
             "-" * (max_phone_number_length + 2), "-" * (max_email_length + 2),
             "-" * (max_birthday_length + 2))

    print(separator_line)

    for i, contact in enumerate(contacts, start=1):
        name = contact.get('name', '')[:max_name_length]
        surname = contact.get('surname', '')[:max_surname_length]
        phone_number = contact.get('phone_number', '')[:max_phone_number_length]
        email = contact.get('email', '')[:max_email_length]
        birthday = contact.get('birthday', '')[:max_birthday_length]
        print("| {:^5} | {:^{}} | {:^{}} | {:^{}} | {:^{}} | {:^{}} |".format(
            i, name, max_name_length, surname, max_surname_length, phone_number,
            max_phone_number_length, email, max_email_length, birthday, max_birthday_length))

        print(separator_line)


def contact_edit_delete_menu(contact_book_manager, field, value, _id=None):
    while True:
        print("\n===== Choose option =====")
        print("1. Edit Contact")
        print("2. Delete Contact")
        print("3. Back to Manage Contacts")
        edit_delete_choice = str(input("Choose option (1/2/3): "))
        if edit_delete_choice == '1':
            if _id is not None:
                edit_contact_by_criteria(contact_book_manager, field, _id)
            else:
                edit_contact(contact_book_manager, field, value)
            break
        elif edit_delete_choice == '2':
            if _id is not None:
                delete_contact(contact_book_manager, "_id", _id)
            else:
                delete_contact(contact_book_manager, field, value)
            break
        elif edit_delete_choice == '3':
            print("Back to Manage Contacts.")
            break
        else:
            print("Invalid choice. Choose an option from 1 to 3.")

def edit_contact(contact_book_manager, field, value):
    new_value = input(f"Enter the new value for {field}: ")
    new_value = new_value.capitalize()
    contact_book_manager.edit(field, value, {field: new_value})
    print("Contact edited successfully.")


def edit_contact_by_criteria(contact_book_manager, field, _id):
    new_value = input(f"Enter the new value for {field}: ")
    new_value = new_value.capitalize()
    search_criteria = {"_id": _id}
    updates = {field: new_value}
    contact_book_manager.edit_by_criteria(search_criteria, updates)
    print("Contact edited successfully.")


def delete_contact(contact_book_manager, field, value):
    contact_book_manager.delete(field, value)
    print("Contact deleted successfully.")