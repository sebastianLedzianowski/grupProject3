from src.utils.sms_api import *

def test_send_sms():
    phone_number = "781087866"
    text_message = "To wiadomosc testowa przy pomocy test_send_sms"
    sms_api(phone_number, text_message)

if __name__ == "__main__":
    test_send_sms()