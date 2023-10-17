import os
import requests
from data_manager import DataManager
# from pprint import pprint
from datetime import datetime, timedelta
# Somehow, I hit my limit of debugging on both using Search API & Multicity API
# I gonna use dr.Angela's method: Using Locations API:

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ.get("TEQUILA_APIKEY")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    # def __init__(self, data_manager: DataManager):
    #     self.sheet = data_manager
        # self.url = "https://api.tequila.kiwi.com/v2/search"
        # self.apikey = os.environ.get("TEQUILA_APIKEY")
        # self.header = {
        #     "apikey": self.apikey
        # }
        # self.config = {}
        # self.family_members = 2
        # self.fly_from_date = datetime.now().strftime("%d/%m/%Y")
        # self.fly_to_date = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")
        # Somehow, I hit my limit of debugging on both using Search API & Multicity API
        # I gonna use dr.Angela's method: Using Locations API:



    def get_requests(self):
        # for item in self.sheet.data:
        #     self.config = {
        #         "requests": []
        #     }
        #     multicity_request = {
        #         "fly_to": item['arriveIataCode'],
        #         "fly_from": item['departIataCode'],
        #         "date_from": self.fly_from_date,
        #         "date_to": self.fly_to_date,
        #         "nights_in_dst_from": 30,
        #         "nights_in_dst_to": 90,
        #         "one_for_city": 1,
        #         "selected_cabins": "W",
        #         "mix_with_cabins": "M",
        #         "adult_hold_bag": "2,2",
        #         "adult_hand_bag": "1,1",
        #         "curr": "USD",
        #         "adults": self.family_members
        #     }
        #     self.config["requests"].append(multicity_request)
        #     response = requests.get(self.url, headers=self.header, params=self.config)
        #     print(response.status_code)
        # return response.json()
        # return pprint(response.json())
        # Somehow, I hit my limit of debugging on both using Search API & Multicity API
        # I gonna use dr.Angela's method: Using Locations API:
        