import os
import requests
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_data import FlightData
from pprint import pprint

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, data_manager: DataManager):
        self.sheet = data_manager

        self.url = "https://tequila-api.kiwi.com/v2/search"
        self.apikey = os.environ.get("TEQUILA_APIKEY")
        self.header = {
            "apikey": self.apikey
        }

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
        try:
            data = response.json()["data"][0]
            print(pprint(data))
        except IndexError:
            print(f"No flights found for {a_iata}.")
            return None

        # flight_data = FlightData(
        #     price=data["price"],
        #     origin_city=data["route"][0]["cityFrom"],
        #     origin_airport=data["route"][0]["flyFrom"],
        #     destination_city=data["route"][0]["cityTo"],
        #     destination_airport=data["route"][0]["flyTo"],
        #     out_date=data["route"][0]["local_departure"].split("T")[0],
        #     return_date=data["route"][1]["local_departure"].split("T")[0]
        # )
        # print(f"{flight_data.destination_city}: USD{flight_data.price}")
        # return flight_data
        print(f"{d_iata} --> {a_iata}: USD{data['price']}")




if __name__ == "__main__":
    data_manager = DataManager()
    flight_search = FlightSearch(data_manager)

