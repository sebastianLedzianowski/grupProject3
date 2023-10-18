from src.utils.contact_book.contact_book_manager import ContactBookManager
from src.utils.notes_book.notesbook_manager import NotesBookManager
from src.utils.contact_book.contact_book_collector import ContactBookCollector
from src.utils.notes_book.notesbook_collector import NotesBookCollector


def main():
    contact_book_manager = ContactBookManager()
    notes_book_manager = NotesBookManager()

    while True:
        print("\n===== Main Menu =====")
        print("1. Manage Contacts")
        print("2. Manage Notes")
        print("3. Exit Program")

        try:
            choice = int(input("Choose option (1/2/3): "))
        except ValueError:
            print("Error! Enter a number.")
            continue

        if choice == 1:
            contact_menu(contact_book_manager)
        elif choice == 2:
            notes_menu(notes_book_manager)
        elif choice == 3:
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
                template = "| {:^17} | {:^17} | {:^17} | {:^30} | {:^15} |"
                header = " Contacts "
                print("{:^90}".format(header.center(110)))
                print("")
                print(template.format("Name", "Surname", "Phone number", "Email", "Birthday"))
                for contact in contacts:
                    formatted_template = template.format(contact["name"], contact["surname"], contact["phone_number"],
                                                         contact["email"], contact["birthday"])
                    print("-" * len(formatted_template))
                    print(formatted_template)
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
                        template = "| {:^17} | {:^17} | {:^17} | {:^30} | {:^15} |"
                        header = f" Sorted Contacts by {sort_key} "
                        print("\n{:-^90}".format(header.center(90)))
                        print(template.format("Name", "Surname", "Phone number", "Email", "Birthday"))
                        for contact in sorted_contacts:
                            formatted_template = template.format(
                                contact["name"], contact["surname"], contact["phone_number"], contact["email"],
                                contact["birthday"]
                            )
                            print("-" * len(formatted_template))
                            print(formatted_template)
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
            if not notes:
                print("No notes found.")
            else:
                template = "| {:^20} | {:^20} | {:^40} |"
                header = " Notes "
                print("\n{:-^90}".format(header.center(90)))
                print(template.format("Title", "Content", "Tags"))
                for note in notes:
                    if isinstance(note, dict):
                        title = note.get("title", "")
                        content = note.get("content", "")
                        tags = ", ".join(note.get("tag", []))
                        formatted_template = template.format(title, content, tags)
                        print("-" * len(formatted_template))
                        print(formatted_template)
                    else:
                        print("Invalid note format.")
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
                if not sorted_notes:
                    print("No notes found.")
                else:
                    template = "| {:^20} | {:^20} | {:^40} |"
                    header = f" Sorted Notes by {sort_key} "
                    print("\n{:-^90}".format(header.center(90)))
                    print(template.format("Title", "Tag", "Content"))
                    for note in sorted_notes:
                        if isinstance(note, dict):
                            title = note.get("title", "")
                            content = note.get("content", "")
                            tags = ", ".join(note.get("tag", []))
                            formatted_template = template.format(title, content, tags)
                            print("-" * len(formatted_template))
                            print(formatted_template)
                        else:
                            print("Invalid note format.")
            elif sort_choice == 4:
                print("Back to Manage Notes.")
            else:
                print("Invalid choice. Choose an option from 1 to 4.")

        elif notes_choice == 6:
            print("Back to Main Menu.")
            break
        else:
            print("Invalid choice. Choose an option from 1 to 6.")


if __name__ == '__main__':
    main()