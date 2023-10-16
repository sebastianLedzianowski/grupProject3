from src.utils.contact_book.contact_book_manager import ContactBookManager
from src.utils.notes_book.notesbook_manager import NotesBookManager
from src.utils.contact_book.contact_book_collector import ContactBookCollector
from src.utils.notes_book.notesbook_collector import NotesBookCollector



def main():
    contact_book_manager = ContactBookManager()
    notes_book_manager = NotesBookManager()

    while True:
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
            contact_book_manager.read_all()
        elif contact_choice == 2:
            user_data = ContactBookCollector.get_user_input()
            contact_book_manager.create(user_data)
        elif contact_choice == 3:
            field = input("Enter the field to edit (e.g., name): ")
            value = input("Enter the current value of the field: ")
            updates = input("Enter the new value for the field: ")
            contact_book_manager.edit(field, value, updates)
        elif contact_choice == 4:
            field = input("Enter the field to delete (e.g., name): ")
            value = input("Enter the value of the field to delete: ")
            contact_book_manager.delete(field, value)
        elif contact_choice == 5:
            sort_key = input("Enter the field to sort contacts by (e.g., name): ")
            sorted_contacts = contact_book_manager.get_sorted_contacts(sort_key)
            for contact in sorted_contacts:
                print(contact)
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
            notes_book_manager.read_all()
        elif notes_choice == 2:
            user_data = NotesBookCollector.get_user_input()
            notes_book_manager.create(user_data)
        elif notes_choice == 3:
            field = input("Enter the field to edit (e.g., title): ")
            value = input("Enter the current value of the field: ")
            new_value = input("Enter the new value for the field: ")
            notes_book_manager.edit(field, value, new_value)
        elif notes_choice == 4:
            field = input("Enter the field to delete (e.g., title): ")
            value = input("Enter the value of the field to delete: ")
            notes_book_manager.delete(field, value)
        elif notes_choice == 5:
            sort_key = input("Enter the field to sort notes by (e.g., title): ")
            sorted_notes = notes_book_manager.sorted(sort_key)
            for note in sorted_notes:
                print(note)
        elif notes_choice == 6:
            print("Back to Main Menu.")
            break
        else:
            print("Invalid choice. Choose an option from 1 to 6.")

if __name__ == '__main__':
    main()