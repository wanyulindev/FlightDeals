import os
import requests
from data_manager import DataManager
# from pprint import pprint
from datetime import datetime

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, data_manager: DataManager):
        self.sheet = data_manager
        self.url = "https://api.tequila.kiwi.com/v2/flights_multi"
        self.apikey = os.environ.get("TEQUILA_APIKEY")
        self.header = {
            # "accept": "application/json",
            "apikey": self.apikey
            # "Content-Type": "application/json"
        }
        self.config = {
            "requests": []
        }
        self.family_members = 2
        # self.current_date = datetime.now().strftime("%d/%m/%Y")
        self.current_date = datetime.now().strftime("%Y-%m-%d")

    def post_requests(self):
        for item in self.sheet.data:
            multicity_request = {
                "fly_to": item['arriveIataCode'],
                "fly_from": item['departIataCode'],
                "date_from": self.current_date,
                # "date_to": self.current_date,
                "adults": self.family_members
            }
            self.config["requests"].append(multicity_request)
        response = requests.post(self.url, headers=self.header, json=self.config)
        return response.status_code
        # return response.json()
        # return pprint(response.json())