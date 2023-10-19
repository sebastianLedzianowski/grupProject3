from src.utils.send_email import *

def test_send_email():
    email = 'including@o2.pl'
    title = 'Temat test'
    content = """
    tresc testowa\nDlaczego\ntak sie \ndzieje
    """
    send_email(email, title, content)

if __name__ == '__main__':
    test_send_email()