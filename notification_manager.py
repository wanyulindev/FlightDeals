from twilio.rest import Client
import os
import time

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        self.account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        self.phone_from = os.environ.get("TWILIO_PHONE_FROM")
        self.phone_to = os.environ.get("TWILIO_PHONE_TO")

    def send_sms(self, message):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
            from_=self.phone_from,
            body=message,
            to=self.phone_to
        )
        # print(message.status)
        print(message.sid)
        time.sleep(10)


