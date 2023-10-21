from src.utils.notes_book.notesbook_collector import NotesBookCollector

def notes_menu(notes_book_manager):
    while True:
        print("\n===== Manage Notes =====")
        print("1. Display Notes")
        print("2. Add Note")
        print("3. Choose Note to Edit/Delete")
        print("4. Sort Notes")
        print("5. Back to Main Menu")
        notes_choice = str(input("Choose option (1/2/3/4/5/6): "))
        if notes_choice == '1':
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
        elif notes_choice == '2':
            user_data = NotesBookCollector.get_user_input()
            notes_book_manager.create(user_data)
        elif notes_choice == '3':
            choose_note(notes_book_manager)
        elif notes_choice == '4':
            print("\n===== Sort Notes =====")
            print("1. Sort by Title")
            print("2. Sort by Tag")
            print("3. Sort by Content")
            print("4. Back to Manage Notes")
            sort_choice = str(input("Choose sort option (1/2/3/4): "))
            if sort_choice.isdigit() and int(sort_choice) in range(1, 4):
                fields = ["title", "tag", "content"]
                sort_key = fields[int(sort_choice) - 1]
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
            elif sort_choice == '4':
                print("Back to Manage Notes.")
            else:
                print("Invalid choice. Choose an option from 1 to 4.")
        elif notes_choice == '5':
            print("Back to Main Menu.")
            break
        else:
            print("Invalid choice. Choose an option from 1 to 6.")


def choose_note(notes_book_manager):
    while True:
        print("\n===== Choose Note by =====")
        print("1. Choose by Title")
        print("2. Choose by Tag")
        print("3. Choose by Content")
        print("4. Back to Manage Notes Menu")
        choice = str(input("Choose edit option (1/2/3/4): "))
        if choice.isdigit() and int(choice) in range(1, 4):
            fields = ["title", "tag", "content"]
            field = fields[int(choice) - 1]
            value = input(f"Enter the current value of the {field}: ")
            duplicates = notes_book_manager.look_for_doubles(field, value)

            if duplicates:
                print("Duplicates found. Choose a duplicate to edit:")
                display_numbered_notes(duplicates)
                chosen_duplicate = str(input("Choose the duplicate to edit (1/2/...): "))
                chosen_duplicate_index = int(chosen_duplicate) - 1
                if 0 <= chosen_duplicate_index < len(duplicates):
                    _id = duplicates[chosen_duplicate_index]["_id"]
                    note_edit_delete_menu(notes_book_manager, field, value, _id)
                else:
                    print("Invalid choice. No note edited.")

            else:
                all_notes = notes_book_manager.read_all()
                matching_notes = [note for note in all_notes if note[field] == value]

                if not matching_notes:
                    print(f"No note found with {field} = {value}. Please choose a valid note.")
                else:
                    print(f"Found a single note with {field} = {value}:")
                    display_numbered_notes(matching_notes)
                    note_edit_delete_menu(notes_book_manager, field, value)
            break
        elif choice == '4':
            print("Back to Choose Note Menu.")
            break
        else:
            print("Invalid choice. Choose an option from 1 to 4.")


def display_numbered_notes(notes):
    note_number = 1
    for note in notes:
        title = note.get("title", "")
        tags = ", ".join(note.get("tag", []))
        content = note.get("content", "")
        print(f'\nNote Number: {note_number}')
        print(f'Title: {title}')
        print(f'Tags: {tags}')
        print(f'Content: {content}')
        note_number += 1


def note_edit_delete_menu(notes_book_manager, field, value, _id=None):
    while True:
        print("\n===== Choose option =====")
        print("1. Edit Note")
        print("2. Delete Note")
        print("3. Back to Manage Notes")
        edit_delete_choice = str(input("Choose option (1/2/3): "))
        if edit_delete_choice == '1':
            if _id is not None:
                edit_note_by_criteria(notes_book_manager, field, _id)
            else:
                edit_note(notes_book_manager, field, value)
            break
        elif edit_delete_choice == '2':
            if _id is not None:
                delete_note(notes_book_manager, "_id", _id)
            else:
                delete_note(notes_book_manager, field, value)
            break
        elif edit_delete_choice == '3':
            print("Back to Manage Notes.")
            break
        else:
            print("Invalid choice. Choose an option from 1 to 3.")


def edit_note(notes_book_manager, field, value):
    new_value = input(f"Enter the new value for {field}: ")
    notes_book_manager.edit(field, value, {field: new_value})
    print("Contact edited successfully.")


def edit_note_by_criteria(notes_book_manager, field, _id):
    new_value = input(f"Enter the new value for {field}: ")
    search_criteria = {"_id": _id}
    updates = {field: new_value}
    notes_book_manager.edit_by_criteria(search_criteria, updates)
    print("Contact edited successfully.")


def delete_note(notes_book_manager, field, value):
    notes_book_manager.delete(field, value)
    print("Contact deleted successfully.")
