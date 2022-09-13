from email import message
import os
import smtplib
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv("./Python Env/env/.env")


TWILIO_SID=os.getenv("TWILIO_SID")
TWILIO_AUTH=os.getenv("TWILIO_AUTH")
TWILIO_NUMB=os.getenv("TWILIO_NUMB")
VERIFIED_NUMB=os.getenv("VERIFIED_NUMB")
SMTP_ADD=os.getenv("SMTP_ADD")
MY_EMAIL=os.getenv("MY_EMAIL")
MY_PASSWORD=os.getenv("MY_PASSWORD")
TO_EMAIL=os.getenv("TO_EMAIL")


class NotificationManager:
    def __init__(self):
        self.client=Client(TWILIO_SID,TWILIO_AUTH)
    def send_msg(self,message):
        message=self.client.message.create(
            body=message,
            from_=TWILIO_NUMB,
            to_=VERIFIED_NUMB,
        )
        print(message.sid)


    def send_emails(self,emails):
        with smtplib.SMTP(SMTP_ADD) as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=TO_EMAIL,
                    msg=f"Subject:New Low Price Flight!\n\n{message}"
                )
