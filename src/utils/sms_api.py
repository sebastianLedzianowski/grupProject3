import os

from dotenv import load_dotenv
from smsapi.client import SmsApiPlClient

def sms_api(phone_number, text_message):

    load_dotenv()
    client = SmsApiPlClient(access_token=os.getenv("TOKEN_API"))

    send_results = client.sms.send(to=phone_number, message=text_message)

    for result in send_results:
        print(result.id, result.points, result.error)