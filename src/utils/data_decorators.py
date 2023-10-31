import os
import re
from datetime import datetime
import kickbox
from dotenv import load_dotenv


def validate_input(prompt):
    def decorator(func):
        def wrapper():
            while True:
                func()
                user_input = input(prompt).strip()
                if not user_input:
                    print("Input is empty. Please provide some input.")
                else:
                    formatted_input = user_input.capitalize()
                    return formatted_input

        return wrapper

    return decorator


def validate_phone_number(func):
    def wrapper():
        while True:
            func()
            phone_number = input('Enter phone number: ')
            pattern = r"(\[4][8]\s)?\d{3}\s\d{3}\s\d{3}"
            if re.fullmatch(pattern, phone_number):
                return phone_number
            else:
                print('Wrong phone number format. Sample number: "123 456 789" or "48 123 456 789"')

    return wrapper


def validate_email(func):
    def wrapper():
        load_dotenv()
        client = kickbox.Client(os.getenv("API_KEY"))
        kbx = client.kickbox()
        while True:
            func()
            email = input('Enter email: ')
            pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if re.match(pattern, email):
                response = kbx.verify(email)
                return response.body['result'] != "undeliverable"
            else:
                print('Invalid email address. Example email: "silmple_adres@example.com"')

    return wrapper


def validate_date(func):
    def wrapper():
        while True:
            func()
            birthday = input('Enter birthday [YYYY-MM-DD]: ')
            try:
                datetime.strptime(birthday, '%Y-%m-%d')
                return birthday
            except ValueError:
                print('Wrong date format. Correct format is "YYYY-MM-DD"')

    return wrapper
