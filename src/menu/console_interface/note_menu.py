from src.utils.notes_book.notes_book_collector import NotesBookCollector


def notes_menu(notes_book_manager, user_interface, manage_notes_abc, sort_choice_abc, choose_note_abc,
               note_edit_delete_menu_abc):
    while True:
        manage_notes_abc.display()
        notes_choice = manage_notes_abc.user_choice()
        if notes_choice == '1':
            notes = notes_book_manager.read_all()
            note_number = 1
            if not notes:
                user_interface.display_print("No notes found.")
            else:
                for note in notes:
                    title = note.get("title", "")
                    tags = ", ".join(note.get("tag", []))
                    content = note.get("content", "")
                    user_interface.display_print(f'\nNote Number: {note_number}')
                    user_interface.display_print(f'Title: {title}')
                    user_interface.display_print(f'Tags: {tags}')
                    user_interface.display_print(f'Content: {content}')
                    note_number += 1
        elif notes_choice == '2':
            user_data = NotesBookCollector.get_user_input()
            notes_book_manager.create(user_data)
        elif notes_choice == '3':
            choose_note(notes_book_manager, user_interface, choose_note_abc, note_edit_delete_menu_abc)
        elif notes_choice == '4':
            sort_choice_abc.display()
            sort_choice = sort_choice_abc.user_choice()
            if sort_choice.isdigit() and int(sort_choice) in range(1, 4):
                fields = ["title", "tag", "content"]
                sort_key = fields[int(sort_choice) - 1]
                sorted_notes = notes_book_manager.sorted(sort_key)
                note_number = 1
                if not sorted_notes:
                    user_interface.display_print("No notes found.")
                else:
                    for note in sorted_notes:
                        title = note.get("title", "")
                        tags = ", ".join(note.get("tag", []))
                        content = note.get("content", "")
                        user_interface.display_print(f'\nNote Number: {note_number}')
                        user_interface.display_print(f'Title: {title}')
                        user_interface.display_print(f'Tags: {tags}')
                        user_interface.display_print(f'Content: {content}')
                        note_number += 1
            elif sort_choice == '4':
                user_interface.display_print("Back to Manage Notes.")
            else:
                user_interface.display_print("Invalid choice. Choose an option from 1 to 4.")
        elif notes_choice == '5':
            user_interface.display_print("Back to Main Menu.")
            break
        else:
            user_interface.display_print("Invalid choice. Choose an option from 1 to 6.")


def choose_note(notes_book_manager, user_interface, choose_note_abc, note_edit_delete_menu_abc):
    while True:
        choose_note_abc.display()
        choice = choose_note_abc.user_choice()
        if choice.isdigit() and int(choice) in range(1, 4):
            fields = ["title", "tag", "content"]
            field = fields[int(choice) - 1]
            value = user_interface.user_choice_input(input(f"Enter the current value of the {field}: "))
            duplicates = notes_book_manager.look_for_doubles(field, value)

            if duplicates:
                user_interface.display_print("Duplicates found. Choose a duplicate to edit:")
                display_numbered_notes(duplicates, user_interface)
                chosen_duplicate = user_interface.user_choice_input(
                    str(input("Choose the duplicate to edit (1/2/...): ")))
                chosen_duplicate_index = int(chosen_duplicate) - 1
                if 0 <= chosen_duplicate_index < len(duplicates):
                    _id = duplicates[chosen_duplicate_index]["_id"]
                    note_edit_delete_menu(notes_book_manager, field, value, note_edit_delete_menu_abc, _id)
                else:
                    user_interface.display_print("Invalid choice. No note edited.")

            else:
                all_notes = notes_book_manager.read_all()
                matching_notes = [note for note in all_notes if note[field] == value]

                if not matching_notes:
                    user_interface.display_print(f"No note found with {field} = {value}. Please choose a valid note.")
                else:
                    user_interface.display_print(f"Found a single note with {field} = {value}:")
                    display_numbered_notes(matching_notes, user_interface)
                    note_edit_delete_menu(notes_book_manager, field, value, user_interface, note_edit_delete_menu_abc)
            break
        elif choice == '4':
            user_interface.display_print("Back to Choose Note Menu.")
            break
        else:
            user_interface.display_print("Invalid choice. Choose an option from 1 to 4.")


def display_numbered_notes(notes, user_interface):
    note_number = 1
    for note in notes:
        title = note.get("title", "")
        tags = ", ".join(note.get("tag", []))
        content = note.get("content", "")
        user_interface.display_print(f'\nNote Number: {note_number}')
        user_interface.display_print(f'Title: {title}')
        user_interface.display_print(f'Tags: {tags}')
        user_interface.display_print(f'Content: {content}')
        note_number += 1


def note_edit_delete_menu(notes_book_manager, field, value, user_interface, note_edit_delete_menu_abc, _id=None):
    while True:
        note_edit_delete_menu_abc.display()
        edit_delete_choice = note_edit_delete_menu_abc.user_choice()
        if edit_delete_choice == '1':
            if _id is not None:
                edit_note_by_criteria(notes_book_manager, field, user_interface, _id)
            else:
                edit_note(notes_book_manager, field, value, user_interface)
            break
        elif edit_delete_choice == '2':
            if _id is not None:
                delete_note(notes_book_manager, user_interface, "_id", _id)
            else:
                delete_note(notes_book_manager, field, value, user_interface)
            break
        elif edit_delete_choice == '3':
            user_interface.display_print("Back to Manage Notes.")
            break
        else:
            user_interface.display_print("Invalid choice. Choose an option from 1 to 3.")


def edit_note(notes_book_manager, field, value, user_interface):
    new_value = user_interface.user_choice_input(input(f"Enter the new value for {field}: "))
    notes_book_manager.edit(field, value, {field: new_value})
    user_interface.display_print("Contact edited successfully.")


def edit_note_by_criteria(notes_book_manager, field, user_interface, _id):
    new_value = user_interface.user_choice_input(input(f"Enter the new value for {field}: "))
    search_criteria = {"_id": _id}
    updates = {field: new_value}
    notes_book_manager.edit_by_criteria(search_criteria, updates)
    user_interface.dispaly_print("Contact edited successfully.")


def delete_note(notes_book_manager, field, value, user_interface):
    notes_book_manager.delete(field, value)
    user_interface.display_print("Contact deleted successfully.")
