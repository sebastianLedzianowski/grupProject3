import re
from datetime import datetime

def validate_phone_number(func):
    def wrapper(*args, **kwargs):
        phone_number = args[2]
        pattern = r"\d{9}"
        if re.match(pattern, phone_number):
            return func(*args, **kwargs)
        else:
            return f'Wrong phone number. Sample number: "123456789"'
    return wrapper

def validate_e_mail(func):
    def wrapper(*args, **kwargs):
        e_mail = args[3]
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern, e_mail):
            return func(*args, **kwargs)
        else:
            return f'Bad email. Example email address: "silmple_adres@ios.com"'
    return wrapper

def is_valid_date(func):
    def wrapper(*args, **kwargs):
        birthday = args[4]
        try:
            datetime.strptime(birthday, '%Y-%m-%d')
            return func(*args, **kwargs)
        except ValueError:
            return f'Wrong date of birth. Correct format "yyyy-mm-dd"'
    return wrapper