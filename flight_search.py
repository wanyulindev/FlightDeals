import os
import requests
from data_manager import DataManager
from pprint import pprint
from datetime import datetime, timedelta
# Somehow, I hit my limit of debugging on both using Search API & Multicity API
# I gonna use dr.Angela's method: Using Locations API:

# TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
# TEQUILA_API_KEY = os.environ.get("TEQUILA_APIKEY")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, data_manager: DataManager):
        self.sheet = data_manager
        # self.url = "https://api.tequila.kiwi.com/v2/search"
        self.url = "https://tequila-api.kiwi.com/v2/search"
        self.apikey = os.environ.get("TEQUILA_APIKEY")
        self.header = {
            "apikey": self.apikey
        }
        # self.config = {
        #     "requests": []
        # }
        self.config = {}
        self.family_members = 2
        self.fly_from_date = datetime.now().strftime("%d/%m/%Y")
        self.fly_to_date = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")
        # Somehow, I hit my limit of debugging on both using Search API & Multicity API
        # I gonna use dr.Angela's method: Using Locations API: (Downstairs)


    def get_requests(self, a_iata, d_iata):
    # for item in self.sheet.data:
        # multicity_request = {
        self.config = {
            "fly_to": a_iata,
            "fly_from": d_iata,
            "date_from": self.fly_from_date,
            "date_to": self.fly_to_date,
            "nights_in_dst_from": 30,
            "nights_in_dst_to": 90,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "selected_cabins": "W",
            "mix_with_cabins": "M",
            "adult_hold_bag": "2,2",
            "adult_hand_bag": "1,1",
            "curr": "USD",
            "adults": self.family_members
        }
        # self.config["requests"].append(multicity_request)
        response = requests.get(self.url, headers=self.header, params=self.config)
        # return response.status_code
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {a_iata}.")
            return None



        # return pprint(response.json())


        # Somehow, I hit my limit of debugging on both using Search API & Multicity API
        # I gonna use dr.Angela's method: Using Locations API to test it out whether
        # it's my codes got problem or i just don't have certain flight to book:

        # location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        # headers = {"apikey": TEQUILA_API_KEY}
        # query = {"term": city_name, "location_types": "city"}
        # response = requests.get(url=location_endpoint, headers=headers, params=query)
        # results = response.json()["locations"]
        # # return response.status_code
        # # return pprint(response.json())
        # code = results[0]["code"]
        # return code

        # Okay, it looks just fine! Let's just test it out why search API got 400 to me:
        # (Back to the search API part): (Upstairs)