import os
import requests
from data_manager import DataManager
from pprint import pprint
from datetime import datetime

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, data_manager: DataManager):
        self.sheet = data_manager
        self.url = "https://api.tequila.kiwi.com/v2/flights_multi"
        self.apikey = os.environ.get("TEQUILA_APIKEY")
        self.header = {
            "apikey": self.apikey
        }
        self.config = {
            "requests": []
        }
        self.family_members = 2
        self.current_date = datetime.now().strftime("%d/%m/%Y")

    def post_requests(self):
        for item in self.sheet.data:
            json_data = {
                "fly_to": item['arriveIataCode'],
                "fly_from": item['departIataCode'],
                "date_from": self.current_date,
                "date_to": self.current_date,
                "adults": self.family_members
            }
            self.config["requests"].append(json_data)
        response = requests.post(self.url, headers=self.header, json=self.config)
        return pprint(response.json())