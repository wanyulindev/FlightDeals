#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

from data_manager import DataManager

data_manager = DataManager()
print(data_manager.get_data())
# sheet_data = data_manager.get_data()
# print(sheet_data)




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