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

    # Instead creating two similar function,
    # why not create a function but can be used as *arg:
    # def get_data(self):
    #     # get_response = requests.get(ENDPOINT, headers=HEADERS)
    #     get_response = requests.get(self.url, headers=self.headers)
    #     self.data = get_response.json()
    #     return pprint(self.data)
    #     # return self.get_response.text
    #     # print(self.get_response.json())

    # Let's separate these two function and maintain codes as clean codes:
    # def data_function(self, func, url):
    #     response = func(url)
    #     if response.status_code == 200:
    #         self.data = response.json()
    #         if self.data and "prices" in self.data:
    #             prices = self.data["prices"]
    #             if prices and len(self.data) > 1:
    #                 last_item = prices[-1]
    #                 self.data_count = last_item.get("id")
    #                 # self.data_count = self.data[0][-1]["id"]
    #                 # return self.data_count
    #                 return self.data_count, pprint(self.data)
    #                 # return self.data_count
    #     return None
        # return pprint(self.data)
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

    def add_data(self, dpt, arv, d_iata, a_iata):
        data_config = {
            "price": {
                'arrival': arv,
                'arriveIataCode': a_iata,
                'departIataCode': d_iata,
                'departure': dpt
            }
        }
        self.data_function(func=requests.post, url=self.url, json=data_config)

    def update_data(self, lowest_price):
        data_config = {
            "price": {
                'lowestPrice': lowest_price
            }
        }
        self.data_function(func=requests.put, url=self.url, json=data_config)



    # def delete_data(self):
        # for _ in self.data["prices"]:
        #     self.data_count += 1
        # self.data_count = self.data[0][-1]["id"]
        # print(self.data_count)
        # for _ in range(self.data_count):
        #     self.data_function(func=requests.delete, url=f"{self.url}/{self.data_count}")
        #     if self.data_count > 1:
        #         self.data_count -= 1
        # return pprint(self.data)

        # self.data_function(func=requests.delete, url=f"{self.url}/{self.data_count}")

# if __name__ == "__main__":
#     data_manager = DataManager()
#     print("executed")


# Submitting commit! 2023/10/09
# Submitting commit! 2023/10/08
# It's time to review OOP to make it more clear idea to my knowledge!
# (151)