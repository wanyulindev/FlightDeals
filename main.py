#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import requests
# from data_manager import DataManager
# from flight_search import FlightSearch

def main():
    # data_manager = DataManager()
    pass


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
    # Had test out Tequila and figure out it's working:
    # flight_search = FlightSearch()
    # response = flight_search.get_requests("LAX")
    # print(response)

    # flight_search = FlightSearch(data_manager)
    # for item in data_manager.data:
    #     response = flight_search.get_requests(a_iata=item["arriveIataCode"],
    #                                           d_iata=item["departIataCode"])
    #     print(response)

#------------------------------------ Test Search API --------------------------------------------
from flight_search_test import FlightSearch
from datetime import datetime, timedelta
from data_manager_test import DataManager


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    # print(sheet_data)
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )



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