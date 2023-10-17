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
                print("\n{:-^90}".format(header.center(90)))
                print(template.format("Name", "Surname", "Phone number", "Email", "Birthday"))
                for contact in contacts:
                    formatted_template = template.format(contact["name"], contact["surname"], contact["phone_number"],
                                                         contact["email"], contact["birthday"])
                    print("-" * len(formatted_template))
                    print(formatted_template)
        elif contact_choice == 2:
            user_data = ContactBookCollector.get_user_input()
            contact_book_manager.create(user_data)
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
                fields = ["Name", "Surname", "Phone number", "Email", "Birthday"]
                field = fields[edit_choice - 1]
                value = input(f"Enter the current value of the {field}: ")
                updates = input(f"Enter the new value for the {field}: ")
                contact_book_manager.edit(field, value, updates)
            elif edit_choice == 6:
                print("Back to Manage Contacts.")
            else:
                print("Invalid choice. Choose an option from 1 to 6.")
        elif contact_choice == 4:
            field = input("Enter the field to delete (e.g., name): ")
            value = input("Enter the value of the field to delete: ")
            contact_book_manager.delete(field, value)
        elif contact_choice == 5:
            sort_key = input("Enter the field to sort contacts by (e.g., name): ")
            sorted_contacts = contact_book_manager.get_sorted_contacts(sort_key)
            if not sorted_contacts:
                print("No contacts found.")
            else:
                template = "| {:^17} | {:^17} | {:^17} | {:^30} | {:^15} |"
                header = " Contacts "
                print("\n{:-^90}".format(header.center(90)))
                print(template.format("Name", "Surname", "Phone number", "Email", "Birthday"))
                for contact in sorted_contacts:
                    formatted_template = template.format(
                        contact["name"], contact["surname"], contact["phone_number"], contact["email"], contact["birthday"]
                    )
                    print("-" * len(formatted_template))
                    print(formatted_template)
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
                print(template.format("Title", "Tag", "Content"))
                for note in notes:
                    formatted_template = template.format(note["title"], note["tag"], note["content"])
                    print("-" * len(formatted_template))
                    print(formatted_template)
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
                fields = ["Title", "Tag", "Content"]
                field = fields[edit_choice - 1]
                value = input(f"Enter the current value of the {field}: ")
                updates = input(f"Enter the new value for the {field}: ")
                notes_book_manager.edit(field, value, updates)
            elif edit_choice == 4:
                print("Back to Manage Notes.")
            else:
                print("Invalid choice. Choose an option from 1 to 4.")
        elif notes_choice == 4:
            field = input("Enter the field to delete (e.g., title): ")
            value = input("Enter the value of the field to delete: ")
            notes_book_manager.delete(field, value)
        elif notes_choice == 5:
            sort_key = input("Enter the field to sort notes by (e.g., title): ")
            sorted_notes = notes_book_manager.sorted(sort_key)
            if not sorted_notes:
                print("No notes found.")
            else:
                template = "| {:^20} | {:^20} | {:^40} |"
                header = " Sorted Notes "
                print("\n{:-^90}".format(header.center(90)))
                print(template.format("Title", "Tag", "Content"))
                for note in sorted_notes:
                    formatted_template = template.format(note["title"], note["tag"], note["content"])
                    print("-" * len(formatted_template))
                    print(formatted_template)
        elif notes_choice == 6:
            print("Back to Main Menu.")
            break
        else:
            print("Invalid choice. Choose an option from 1 to 6.")


if __name__ == '__main__':
    main()