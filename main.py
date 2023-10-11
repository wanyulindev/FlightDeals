#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import requests
from data_manager import DataManager

# Retrieve origin data from my Google sheet:
data_manager = DataManager()
data_get_origin = data_manager.data_function(func=requests.get, url=data_manager.url)
print(data_get_origin)
# sheet_data = data_manager.get_data()
# print(sheet_data)

# Delete datas I don't need to fit with my desire:
# print(data_manager.delete_data)
execute_delete_data = data_manager.data_function(func=requests.delete,
                                                 url=f"{data_manager.url}/{data_manager.delete_data()}")
print(execute_delete_data)
# print(data_manager.data_function(func=requests.delete,
#                                  url=f"{data_manager.url}/7"))







# Test it out why can't print out: (FIXED!)
# import os
# import requests
#
# # AUTH = os.environ.get("SHEETY_AUTH")
# # ENDPOINT = os.environ.get("SHEETY_URL")
# # HEADERS = {
# #             "Authorization": AUTH
# #         }
#
# get_response = requests.get("https://api.sheety.co/792a621e9a95f9932e7a7e96c1680077/workoutTracking/workouts")
# print(get_response.text)
# # data = get_response.json()
# # print(data)