from src.utils.contact_book.contact_book_collector import ContactBookCollector


def contact_menu(contact_book_manager, user_interface, manage_contacts_abc, sort_contacts_abc, choose_contact_abc,
                 contact_edit_delete_menu_abc):
    while True:
        manage_contacts_abc.display()
        contact_choice = manage_contacts_abc.user_choice()
        match contact_choice:
            case '1':
                contacts = contact_book_manager.read_all()
                display_contacts(contacts, user_interface)
            case '2':
                user_data = ContactBookCollector.get_user_input()
                contact_book_manager.create(user_data)
                user_interface.display_print("Contact added successfully.")
            case '3':
                choose_contact(contact_book_manager, user_interface, choose_contact_abc, contact_edit_delete_menu_abc)
            case '4':
                sort_contact(sort_contacts_abc, user_interface, contact_book_manager)
            case '5':
                user_interface.display_print("Back to Main Menu.")
                break
            case _:
                user_interface.display_print("Invalid choice. Choose an option from 1 to 6.")


def display_contacts(contacts, user_interface):
    if not contacts:
        user_interface.display_print("No contacts found.")
    else:
        max_name_length = max(len(contact.get('name', '')) for contact in contacts)
        max_surname_length = max(len(contact.get('surname', '')) for contact in contacts)
        max_phone_number_length = max(len(contact.get('phone_number', '')) for contact in contacts)
        max_email_length = max(len(contact.get('email', '')) for contact in contacts)
        max_birthday_length = max(len(contact.get('birthday', '')) for contact in contacts)
        user_interface.display_print(
            "\n| {:^{}} | {:^{}} | {:^{}} | {:^{}} | {:^{}} |".format('Name', max_name_length, 'Surname',
                                                                      max_surname_length, 'Phone number',
                                                                      max_phone_number_length, 'Email',
                                                                      max_email_length, 'Birthday',
                                                                      max_birthday_length))
        separator_line = "|{}+{}+{}+{}+{}|".format("-" * (max_name_length + 2), "-" * (max_surname_length + 2),
                                                   "-" * (max_phone_number_length + 2), "-" * (max_email_length + 2),
                                                   "-" * (max_birthday_length + 2))
        user_interface.display_print(separator_line)
        for contact in contacts:
            name = contact.get('name', '')[:max_name_length]
            surname = contact.get('surname', '')[:max_surname_length]
            phone_number = contact.get('phone_number', '')[:max_phone_number_length]
            email = contact.get('email', '')[:max_email_length]
            birthday = contact.get('birthday', '')[:max_birthday_length]
            user_interface.display_print(
                "| {:^{}} | {:^{}} | {:^{}} | {:^{}} | {:^{}} |".format(name, max_name_length, surname,
                                                                        max_surname_length, phone_number,
                                                                        max_phone_number_length, email,
                                                                        max_email_length, birthday,
                                                                        max_birthday_length))
            user_interface.display_print(separator_line)


def choose_contact(contact_book_manager, user_interface, choose_contact_abc, contact_edit_delete_menu_abc):
    while True:
        choose_contact_abc.display()
        choice = choose_contact_abc.user_choice()
        if choice.isdigit() and int(choice) in range(1, 6):
            fields = ["name", "surname", "phone_number", "email", "birthday"]
            field = fields[int(choice) - 1]
            value = user_interface.user_choice_input(input(f"Enter the current value of the {field}: "))
            value = value.capitalize()
            duplicates = contact_book_manager.look_for_doubles(field, value)

            if duplicates:
                if len(duplicates) == 1:
                    user_interface.display_print(f"Found a single contact with {field} = {value}:")
                    display_numbered_contacts([duplicates[0]], user_interface)
                    _id = duplicates[0]["_id"]
                    contact_edit_delete_menu(contact_book_manager, field, value, contact_edit_delete_menu_abc, _id)
                else:
                    user_interface.display_print(f"Duplicates found for {field} = {value}. Choose a duplicate to edit:")
                    display_numbered_contacts(duplicates, user_interface)
                    chosen_duplicate = user_interface.user_input(str(input("Choose the duplicate to edit (1/2/...): ")))
                    chosen_duplicate_index = int(chosen_duplicate) - 1
                    if 0 <= int(chosen_duplicate_index) < len(duplicates):
                        _id = duplicates[int(chosen_duplicate_index)]["_id"]
                        contact_edit_delete_menu(contact_book_manager, field, value, user_interface, _id)
                    else:
                        user_interface.display_print("Invalid choice. No contact edited.")
            else:
                all_contacts = contact_book_manager.read_all()
                matching_contacts = [contact for contact in all_contacts if contact[field] == value]

                if not matching_contacts:
                    user_interface.display_print(
                        f"No contact found with {field} = {value}. Please choose a valid contact.")
                else:
                    user_interface.display_print(f"Found a single contact with {field} = {value}:")
                    display_numbered_contacts(matching_contacts, user_interface)
                    contact_edit_delete_menu(contact_book_manager, field, value, user_interface,
                                             contact_edit_delete_menu_abc)
            break
        elif choice == '6':
            user_interface.display_print("Back to Choose Contact Menu.")
            break
        else:
            user_interface.display_print("Invalid choice. Choose an option from 1 to 6.")


def sort_contact(sort_contacts_abc, user_interface, contact_book_manager):
    sort_contacts_abc.display()
    sort_choice = sort_contacts_abc.user_choice()
    if sort_choice.isdigit() and int(sort_choice) in range(1, 6):
        fields = ["name", "surname", "phone_number", "email", "birthday"]
        sort_key = fields[int(sort_choice) - 1]
        sorted_contacts = contact_book_manager.get_sorted_contacts(sort_key)
        if not sorted_contacts:
            user_interface.display_print("No contacts found.")
        else:
            max_name_length = max(len(contact.get('name', '')) for contact in sorted_contacts)
            max_surname_length = max(len(contact.get('surname', '')) for contact in sorted_contacts)
            max_phone_number_length = max(len(contact.get('phone_number', ''))
                                          for contact in sorted_contacts)
            max_email_length = max(len(contact.get('email', '')) for contact in sorted_contacts)
            max_birthday_length = max(len(contact.get('birthday', '')) for contact in sorted_contacts)
            user_interface.display_print(f"\nSorted Contacts by: {sort_key} ")
            user_interface.display_print(
                "| {:^{}} | {:^{}} | {:^{}} | {:^{}} | {:^{}} |".format('Name', max_name_length, 'Surname',
                                                                        max_surname_length, 'Phone number',
                                                                        max_phone_number_length, 'Email',
                                                                        max_email_length, 'Birthday',
                                                                        max_birthday_length))
            separator_line = "|{}+{}+{}+{}+{}|".format("-" * (max_name_length + 2),
                                                       "-" * (max_surname_length + 2),
                                                       "-" * (max_phone_number_length + 2),
                                                       "-" * (max_email_length + 2),
                                                       "-" * (max_birthday_length + 2))
            user_interface.display_print(separator_line)
            for contact in sorted_contacts:
                name = contact.get('name', '')[:max_name_length]
                surname = contact.get('surname', '')[:max_surname_length]
                phone_number = contact.get('phone_number', '')[:max_phone_number_length]
                email = contact.get('email', '')[:max_email_length]
                birthday = contact.get('birthday', '')[:max_birthday_length]
                user_interface.display_print(
                    "| {:^{}} | {:^{}} | {:^{}} | {:^{}} | {:^{}} |".format(name, max_name_length, surname,
                                                                            max_surname_length,
                                                                            phone_number,
                                                                            max_phone_number_length, email,
                                                                            max_email_length, birthday,
                                                                            max_birthday_length))
                user_interface.display_print(separator_line)
    elif sort_choice == '6':
        user_interface.display_print("Back to Manage Contacts.")
    else:
        user_interface.display_print("Invalid choice. Choose an option from 1 to 6.")

def display_numbered_contacts(contacts, user_interface):
    max_name_length = max(len(contact.get('name', '')) for contact in contacts)
    max_surname_length = max(len(contact.get('surname', '')) for contact in contacts)
    max_phone_number_length = max(len(contact.get('phone_number', '')) for contact in contacts)
    max_email_length = max(len(contact.get('email', '')) for contact in contacts)
    max_birthday_length = max(len(contact.get('birthday', '')) for contact in contacts)

    user_interface.display_print("\n| {:^5} | {:^{}} | {:^{}} | {:^{}} | {:^{}} | {:^{}} |".format(
        'Index', 'Name', max_name_length, 'Surname', max_surname_length, 'Phone number',
        max_phone_number_length, 'Email', max_email_length, 'Birthday', max_birthday_length))

    separator_line = "|{:^7}|{}+{}+{}+{}+{}|".format(
        ' ', "-" * (max_name_length + 2), "-" * (max_surname_length + 2),
             "-" * (max_phone_number_length + 2), "-" * (max_email_length + 2),
             "-" * (max_birthday_length + 2))

    user_interface.display_print(separator_line)

    for i, contact in enumerate(contacts, start=1):
        name = contact.get('name', '')[:max_name_length]
        surname = contact.get('surname', '')[:max_surname_length]
        phone_number = contact.get('phone_number', '')[:max_phone_number_length]
        email = contact.get('email', '')[:max_email_length]
        birthday = contact.get('birthday', '')[:max_birthday_length]
        user_interface.display_print("| {:^5} | {:^{}} | {:^{}} | {:^{}} | {:^{}} | {:^{}} |".format(
            i, name, max_name_length, surname, max_surname_length, phone_number,
            max_phone_number_length, email, max_email_length, birthday, max_birthday_length))

        user_interface.display_print(separator_line)


def contact_edit_delete_menu(contact_book_manager, field, value, user_interface, contact_edit_delete_menu_abc,
                             _id=None):
    while True:
        contact_edit_delete_menu_abc.display()
        edit_delete_choice = contact_edit_delete_menu_abc.user_choice()
        match edit_delete_choice:
            case '1':
                if _id is not None:
                    edit_contact_by_criteria(contact_book_manager, field, user_interface, _id)
                else:
                    edit_contact(contact_book_manager, field, value, user_interface)
                break
            case '2':
                if _id is not None:
                    delete_contact(contact_book_manager, "_id", user_interface, _id)
                else:
                    delete_contact(contact_book_manager, field, value, user_interface)
                break
            case '3':
                user_interface.display_print("Back to Manage Contacts.")
                break
            case _:
                user_interface.display_print("Invalid choice. Choose an option from 1 to 3.")


def edit_contact(contact_book_manager, field, value, user_interface):
    new_value = user_interface.user_choice_input(input(f"Enter the new value for {field}: "))
    new_value = new_value.capitalize()
    contact_book_manager.edit(field, value, {field: new_value})
    user_interface.display_print("Contact edited successfully.")


def edit_contact_by_criteria(contact_book_manager, field, _id, user_interface):
    new_value = user_interface.User_choice_input(input(f"Enter the new value for {field}: "))
    new_value = new_value.capitalize()
    search_criteria = {"_id": _id}
    updates = {field: new_value}
    contact_book_manager.edit_by_criteria(search_criteria, updates)
    user_interface.display_print("Contact edited successfully.")


def delete_contact(contact_book_manager, field, value, user_interface):
    contact_book_manager.delete(field, value)
    user_interface.display_print("Contact deleted successfully.")
