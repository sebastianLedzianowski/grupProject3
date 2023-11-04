from src.utils.send_email import send_email


def check_birthday_menu(contact_book_manager, user_interface):
    upcoming_birthdays = contact_book_manager.get_days_to_birthday
    user_interface.display_print("\n======== Check Days Until Next Birthday ========")
    if not upcoming_birthdays:
        user_interface.display_print("No upcoming birthdays found.")
    else:
        for birthday_info in upcoming_birthdays:
            user_interface.display_print(
                f"{birthday_info['name']} {birthday_info['surname']}'s birthday is in "
                f"{birthday_info['days_to_birthday']} days.")

        for birthday_info in upcoming_birthdays:
            if birthday_info['days_to_birthday'] == 0:
                email = birthday_info['email']
                generate_birthday_wish(contact_book_manager, birthday_info, email, user_interface)


def generate_birthday_wish(contact_book_manager, birthday_info, email, user_interface):
    while True:
        user_interface.display_print(
            f"\nWould you like to generate birthday wishes to {birthday_info['name']} {birthday_info['surname']}?")
        user_interface.display_print("1. Yes")
        user_interface.display_print("2. No")
        user_choice = user_interface.user_choice_input(str(input("Choose option (1/2): ")))
        if user_choice == '1':
            response = contact_book_manager.get_birthday_wish(birthday_info['name'])
            if response and response.status_code == 200:
                wish = response.json()['wish']
                user_interface.display_print("Birthday wishes generated successfully:")
                user_interface.display_print(f'{wish}')
                return handle_send_email(birthday_info, email, wish, user_interface)
            else:
                user_interface.display_print("Error generating birthday wishes.")
        elif user_choice == '2':
            user_interface.display_print(f"Birthday wishes not generated.")
            return
        else:
            user_interface.display_print("Invalid choice. Birthday wishes not generated.")


def handle_send_email(birthday_info, email, wish, user_interface):
    while True:
        user_interface.display_print(f"\nDo you want to send an email with birthday wishes to {birthday_info['name']}?")
        user_interface.display_print("1. Yes")
        user_interface.display_print("2. No")
        user_choice = user_interface.user_choice_input(str(input("Choose option (1/2): ")))
        if user_choice == '1':
            return send_email(email, "Birthday Wishes", wish)
        user_interface.display_print("Invalid input. Please enter a number.\n")
