from src.utils.notes_book.notesbook_manager import NotesBookManager

def read_all_notes_book():
    notes_manager = NotesBookManager()
    notes = notes_manager.read_all()
    if notes:
        print(f"here is the contact list:")
        for note in notes:
            print(note)
    else:
        print(f'No notes in the database.')

if __name__ == '__main__':
    read_all_notes_book()