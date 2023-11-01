import os
import requests
from pprint import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # self.auth = os.environ.get("SHEETY_AUTH")
        self.url = os.environ.get("SHEETY_URL")
        # self.headers = {
        #     "Authorization": self.auth
        # }
        self.data = {}
        self.data_count = 0

    def data_function(self, func, url, json=None):
        response = func(url, json=json)
        if response.status_code == 200:
            self.data = response.json().get("prices", [])
            # .get("prices", []) tries to access the "prices" key within the dictionary.
            # If "prices" is present, it returns the associated value.
            # If "prices" is not present, it returns an empty list ([]) as the default value.
            return f"Data from GoogleSheet: {pprint(self.data)}"

    def retrieve_current_data(self):
        self.data_function(func=requests.get, url=self.url)

    def delete_data(self):
        if len(self.data) > 0:
            last_item = self.data[-1]
            self.data_count = last_item.get("id")
            # self.data_count = self.data[0][-1]["id"]
            # return self.data_count
            self.data_function(func=requests.delete,
                               url=f"{self.url}/{self.data_count}")
            # return self.data_count
        return None

    def add_flight_data(self, dpt, arv, d_iata, a_iata):
        data_config = {
            "price": {
                'arrival': arv,
                'arriveIataCode': a_iata,
                'departIataCode': d_iata,
                'departure': dpt
            }
        }
        self.data_function(func=requests.post, url=self.url, json=data_config)

    def update_lowest_price(self, lowest_price, object_id ):
        data_config = {
            "price": {
                'lowestPrice': lowest_price
            }
        }
        self.data_function(func=requests.put, url=f"{self.url}/{object_id}", json=data_config)

    def add_datetime(self, date_time):
        data_config = {
            "price": {
                'updatedAt': date_time
            }
        }
        self.data_function(func=requests.post, url=self.url, json=data_config)

    def update_datetime(self, date_time, object_id):
        data_config = {
            "price": {
                'updatedAt': date_time
            }
        }
        self.data_function(func=requests.put, url=f"{self.url}/{object_id}", json=data_config)



# if __name__ == "__main__":
#     data_manager = DataManager()
#     print("executed")

