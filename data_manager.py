import requests
import os
from pprint import pprint

# AUTH = os.environ.get("SHEETY_AUTH")
# ENDPOINT = os.environ.get("SHEETY_URL")
# HEADERS = {
#             "Authorization": AUTH
#         }

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # self.auth = os.environ.get("SHEETY_AUTH")
        self.url = os.environ.get("SHEETY_URL")
        # self.headers = {
        #     "Authorization": self.auth
        # }
        # self.get_response = requests.get(self.url, headers=self.headers)
        # self.get_data()
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

    def data_function(self, func, url):
        response = func(url)
        self.data = response.json()
        return pprint(self.data)

    def update_data(self):
        pass

    def delete_data(self):
        # for _ in self.data["prices"]:
        #     self.data_count += 1
        self.data_count = self.data[0][-1]["id"]
        print(self.data_count)
        # for _ in range(self.data_count):
        #     self.data_function(func=requests.delete, url=f"{self.url}/{self.data_count}")
        #     if self.data_count > 1:
        #         self.data_count -= 1
        # return pprint(self.data)

        # self.data_function(func=requests.delete, url=f"{self.url}/{self.data_count}")






# It's time to review OOP to make it more clear idea to my knowledge!
# (151)