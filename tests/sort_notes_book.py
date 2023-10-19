from src.utils.notes_book.notesbook_manager import NotesBookManager

def sort_notes_book(sort_key):
    notes_manager = NotesBookManager()
    notes = notes_manager.sorted(sort_key)
    if notes:
        print(f"here is the sorted list by {sort_key}:")
        for note in notes:
            print(note)
    else:
        print(f'No notes in the database.')

if __name__ == '__main__':
    #sort_notes_book('title')
    #sort_notes_book('tag')
    sort_notes_book('content')
    pass