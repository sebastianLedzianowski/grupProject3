import re
from datetime import datetime

def validate_input(prompt):
    def decorator(func):
        def wrapper():
            while True:
                user_input = input(prompt)
                if user_input.strip():
                    return user_input
                else:
                    print("Invalid input. Please try again.")
        return wrapper
    return decorator


def validate_phone_number(func):
    def wrapper():
        while True:
            phone_number = input('Enter phone number: ')
            pattern = r"(\+[4][8]\s)?\d{3}\s\d{3}\s\d{3}"
            if re.match(pattern, phone_number):
                return phone_number
            else:
                print('Wrong phone number format. Sample number: "123 456 789" or "+48 123 456 789"')
    return wrapper

def validate_email(func):
    def wrapper():
        while True:
            email = input('Enter email: ')
            pattern = r"[a-zA-Z._]+[\w.'']+@\w+[.]\w+\w+"
            if re.match(pattern, email):
                return email
            else:
                print('Invalid email address. Example email: "silmple_adres@example.com"')
    return wrapper

def validate_date(func):
    def wrapper():
        while True:
            birthday = input('Enter birthday [YYYY-MM-DD]: ')
            try:
                datetime.strptime(birthday, '%Y-%m-%d')
                return birthday
            except ValueError:
                print('Wrong date format. Correct format is "YYYY-MM-DD"')
    return wrapper