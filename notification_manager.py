from twilio.rest import Client
import os
# from flight_data import FlightData
from data_manager import DataManager
from flight_data import FlightData
import time

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self, flight_data: FlightData, data_manager: DataManager):
        # self.flight_info = flight_data
        self.sheet = data_manager
        self.flight_info = flight_data

        self.auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        self.account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        self.phone_from = os.environ.get("TWILIO_PHONE_FROM")
        self.phone_to = os.environ.get("TWILIO_PHONE_TO")

    def send_sms(self):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
            from_=self.phone_from,
            body=f"{self.flight_info.origin_airport} --> {self.flight_info.destination_airport} "
                 f"flight, has dropped! Details are as followed:\n"
                 f"Price: USD{self.flight_info.price}, "
                 f"dropped from USD{self.sheet.data['lowestPrice']}.\n"
                 f"Outbound Date: {self.flight_info.out_date}\n"
                 f"Inbound Date: {self.flight_info.return_date}",
            to=self.phone_to
        )
        print(message.status)
        print(message.sid)
        time.sleep(10)

