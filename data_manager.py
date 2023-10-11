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

    # Let's separate these two function and maintain codes as clean codes:
    def data_function(self, func, url):
        response = func(url)
        if response.status_code == 200:
            self.data = response.json()
            if self.data and "prices" in self.data:
                prices = self.data["prices"]
                if prices and len(self.data) > 1:
                    last_item = prices[-1]
                    self.data_count = last_item.get("id")
                    # self.data_count = self.data[0][-1]["id"]
                    # return self.data_count
                    return self.data_count, pprint(self.data)
                    # return self.data_count
        return None
        # return pprint(self.data)

    def update_data(self):
        pass

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

if __name__ == "__main__":
    data_manager = DataManager()


# Submitting commit! 2023/10/09
# Submitting commit! 2023/10/08
# It's time to review OOP to make it more clear idea to my knowledge!
# (151)