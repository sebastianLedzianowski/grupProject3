from src.utils.send_email import send_email


def check_birthday_menu(contact_book_manager):
    upcoming_birthdays = contact_book_manager.get_days_to_birthday
    print("\n======== Check Days Until Next Birthday ========")
    if not upcoming_birthdays:
        print("No upcoming birthdays found.")
    else:
        for birthday_info in upcoming_birthdays:
            print(
                f"{birthday_info['name']} {birthday_info['surname']}'s birthday is in "
                f"{birthday_info['days_to_birthday']} days.")

        for birthday_info in upcoming_birthdays:
            if birthday_info['days_to_birthday'] == 0:
                email = birthday_info['email']
                generate_birthday_wish(contact_book_manager, birthday_info, email)


def generate_birthday_wish(contact_book_manager, birthday_info, email):
    while True:
        print(f"\nWould you like to generate birthday wishes to {birthday_info['name']} {birthday_info['surname']}?")
        print("1. Yes")
        print("2. No")
        user_choice = str(input("Choose option (1/2): "))
        if user_choice == '1':
            response = contact_book_manager.get_birthday_wish(birthday_info['name'])
            if response and response.status_code == 200:
                wish = response.json()['wish']
                print("Birthday wishes generated successfully:")
                print(f'{wish}')
                return handle_send_email(birthday_info, email, wish)
            else:
                print("Error generating birthday wishes.")
        elif user_choice == '2':
            print(f"Birthday wishes not generated.")
            return
        else:
            print("Invalid choice. Birthday wishes not generated.")


def handle_send_email(birthday_info, email, wish):
    while True:
        print(f"\nDo you want to send an email with birthday wishes to {birthday_info['name']}?")
        print("1. Yes")
        print("2. No")
        user_choice = str(input("Choose option (1/2): "))
        if user_choice == '1':
            return send_email(email, "Birthday Wishes", wish)
        print("Invalid input. Please enter a number.\n")