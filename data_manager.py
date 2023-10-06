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
        self.auth = os.environ.get("SHEETY_AUTH")
        self.url = os.environ.get("SHEETY_URL")
        self.headers = {
            "Authorization": self.auth
        }
        # self.get_response = requests.get(self.url, headers=self.headers)
        # self.get_data()
        self.data = {}

    # Instead creating two similar function,
    # why not create a function but can be used as *arg:
    # def get_data(self):
    #     # get_response = requests.get(ENDPOINT, headers=HEADERS)
    #     get_response = requests.get(self.url, headers=self.headers)
    #     self.data = get_response.json()
    #     return pprint(self.data)
    #     # return self.get_response.text
    #     # print(self.get_response.json())

    def data_function(self, func):
        response = func(self.url, headers=self.headers)
        self.data = response.json()
        return pprint(self.data)

    def 





# It's time to review OOP to make it more clear idea to my knowledge!
# (151)