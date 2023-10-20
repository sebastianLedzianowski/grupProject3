from src.utils.contact_book.contact_book_manager import ContactBookManager

cbm = ContactBookManager()


for i in cbm.get_sorted_contacts('phone_number'):
    print(i)