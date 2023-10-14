from src.utils.contact_book.contact_book_manager import ContactBookManager

def read_all_contact_book():
    contact_manager = ContactBookManager()
    contacts = contact_manager.read_all()
    if contacts:
        print(f"Here is the contact list:")
        for contant in contacts:
            print(contant)
    else:
        print(f'No contacts in the database.')
if __name__ == '__main__':
    read_all_contact_book()