# import requests
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData
from datetime import datetime

CURRENT_DATETIME = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def main():
    data_manager = DataManager()

    # Retrieve origin data from my Google sheet:
    # data_get_origin = data_manager.data_function(func=requests.get, url=data_manager.url)
    # print(data_get_origin)
    # (Keep code even more clean this way):
    data_manager.retrieve_current_data()

    # Delete data I don't need to fit with my desire:
    # execute_delete_data = data_manager.data_function(func=requests.delete,
    #                                                  url=f"{data_manager.url}/{data_manager.delete_data()}")
    # print(execute_delete_data)
    # (Rather write it this way): Keep it more clean:
    # data_manager.delete_data()

    # Add new Row in Google Sheet:
    # data_manager.add_flight_data(dpt="Taiwan", arv="Los Angeles", d_iata="TPE", a_iata="LAX")

    # Add new Updated at data in Google Sheet:
    # data_manager.add_datetime(CURRENT_DATETIME)

    # Update - Updated At  in Google Sheet:
    # for item in data_manager.data:
    #     data_manager.update_datetime(date_time=CURRENT_DATETIME,
    #                                  object_id=item["id"])

#----------------------------------------- Google Sheet Finished ---------------------------------------
    # flight_search = FlightSearch()
    # response = flight_search.get_requests("LAX")
    # print(response)
#-------------------------------------------------------------------------------------------------
    flight_search = FlightSearch(data_manager)
    for item in data_manager.data:
        current_flight_price = flight_search.get_requests(a_iata=item["arriveIataCode"],
                                              d_iata=item["departIataCode"])
        # print(current_flight_price)
#------------------------------------------Sending SMS--------------------------------------------
        lowest_price = int(item['lowestPrice'])
        a_city = item['arrival']
        a_iata = item['arriveIataCode']
        d_iata = item['departIataCode']
        d_city = item['departure']

        out_date = flight_search.data['route'][0]['local_departure'][:10]
        return_date = flight_search.data['route'][1]['local_departure'][:10]

        flight_data = FlightData(
            price=current_flight_price,
            origin_city=d_city,
            origin_airport=d_iata,
            destination_city=a_city,
            destination_airport=a_iata,
            out_date=out_date,
            return_date=return_date
        )
        notification_manager = NotificationManager()
        if flight_data.price < lowest_price:
            notification_manager.send_sms(
                message=f"{d_iata} --> {a_iata} price dropped:\n"
                 f"USD{current_flight_price} (dropped from USD{lowest_price})\n"
                 f"from {out_date} to {return_date}\n"
            )
            data_manager.update_lowest_price(lowest_price=current_flight_price,
                                     object_id=item['id'])
            data_manager.update_datetime(date_time=CURRENT_DATETIME,
                                         object_id=item["id"])


main()


# Commit

# Commit 