import os
import requests
from data_manager import DataManager
from datetime import datetime, timedelta

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, data_manager: DataManager):
        self.sheet = data_manager

        self.url = "https://tequila-api.kiwi.com/v2/search"
        self.apikey = os.environ.get("TEQUILA_APIKEY")
        self.header = {
            "apikey": self.apikey
        }
        self.data = {}

    def date_config(self, days):
        return (datetime.now() + timedelta(days=days)).strftime("%d/%m/%Y")


    def get_requests(self, a_iata, d_iata):
        query = {
            "fly_to": a_iata,
            "fly_from": d_iata,
            "date_from": self.date_config(1),
            "date_to": self.date_config(180),
            # "selected_cabins": "W",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        response = requests.get(
            url=self.url,
            headers=self.header,
            params=query
        )
        # Dr. Angela's solution:
        try:
            self.data = response.json()["data"][0]
            # print(pprint(self.data))
        except IndexError:
            print(f"No flights found for {a_iata}.")
            return None

        # GPT's solution:
        # self.data = response.json().get(["data"][0], f"No flights found for {a_iata}.")

        return int(self.data['price'])




if __name__ == "__main__":
    data_manager = DataManager()
    flight_search = FlightSearch(data_manager)

