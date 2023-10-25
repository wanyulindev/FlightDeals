from twilio.rest import Client
import os
from flight_search import FlightSearch
from data_manager import DataManager

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        self.account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        self.phone_from = os.environ.get("TWILIO_PHONE_FROM")
        self.phone_to = os.environ.get("TWILIO_PHONE_TO")

    def send_sms(self):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
            from_=self.phone_from,
            body=f"Your {STOCK} flight, has dropped!\n"
                 f"Details down below:\n"
                 f"Headline: {item['title']}.\n"
                 f"Brief: {item['description']}",
            to=self.phone_to
        )

        print(message.sid)

