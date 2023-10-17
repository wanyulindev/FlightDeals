#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import requests
from data_manager import DataManager
from flight_search import FlightSearch

def main():
    data_manager = DataManager()
    flight_search = FlightSearch(data_manager)

    # Retrieve origin data from my Google sheet:
    # data_get_origin = data_manager.data_function(func=requests.get, url=data_manager.url)
    # print(data_get_origin)
    # (Keep code even more clean this way):
    # data_manager.retrieve_current_data()


    # Delete data I don't need to fit with my desire:
    # execute_delete_data = data_manager.data_function(func=requests.delete,
    #                                                  url=f"{data_manager.url}/{data_manager.delete_data()}")
    # print(execute_delete_data)
    # (Rather write it this way): Keep it more clean:
    # data_manager.delete_data()


    # Add new Row in Google Sheet:
    # data_manager.add_data(dpt="Taiwan", arv="Los Angeles", d_iata="TPE", a_iata="LAX")

#----------------------------------------- Google Sheet Finished ---------------------------------------

    response = flight_search.get_requests()
    print(response)





if __name__ == "__main__":
    main()


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