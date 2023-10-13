import os
import requests
from pprint import pprint
from datetime import datetime

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url = "https://api.tequila.kiwi.com/v2/flights_multi"
        self.apikey = os.environ.get("TEQUILA_APIKEY")
        self.header = {
            "apikey": self.apikey
        }
        self.config = {}

    def post_requests(self):
        self.config = {
            "requests": [
        {
            "fly_to": "LGW",
            "fly_from": "PRG",
            "date_from": "17/08/2023",
            "date_to": "17/08/2023",
            "adults": 1
        },
        {
            "fly_to": "LGW",
            "fly_from": "PRG",
            "date_from": "17/08/2023",
            "date_to": "17/08/2023",
            "adults": 1
        }
        ]
        }
        requests.post(self.url, headers=self.header)