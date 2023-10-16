import os
import smtplib
from email.message import EmailMessage
import ssl
from dotenv import load_dotenv


def send_email(email, title, content):
    load_dotenv()
    name = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASSWD")
    address = 'smtp.gmail.com'
    port = 465
    context = ssl.create_default_context()

# ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED]
# certificate verify failed: unable to get local issuer certificate (_ssl.c:1002)
# sudo /Applications/Python\ 3.11/Install\ Certificates.command

    em = EmailMessage()
    em['From'] = name
    em['To'] = email
    em['Subject'] = title
    em.set_content(content)

    try:
        with smtplib.SMTP_SSL(address, port, context=context) as smtp:
            smtp.login(name, password)
            smtp.sendmail(name, email, em.as_string())
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email. Error: {e}')


