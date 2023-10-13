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
        self.config = {}
        self.family_members = 2

    def post_requests(self):
        for item in self.sheet.data:
            self.config = {
                "requests": [
            {
                "fly_to": item['arriveIataCode'],
                "fly_from": item['departIataCode'],
                "date_from": "17/08/2023",
                "date_to": "17/08/2023",
                "adults": self.family_members
            },
            {
                "fly_to": item,
                "fly_from": "PRG",
                "date_from": "17/08/2023",
                "date_to": "17/08/2023",
                "adults": self.family_members
            }
            ]
            }
            requests.post(self.url, headers=self.header)