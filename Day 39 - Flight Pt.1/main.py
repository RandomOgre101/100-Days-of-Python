from data_manager import DataManager
from pprint import pprint
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager


data_manager = DataManager()
sheet_data = data_manager.get_sheety()
flight_search = FlightSearch()
notification = NotificationManager()

ORIGIN_CITY = "LON"

if sheet_data['prices'][0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data['prices']:
        row['iataCode'] = flight_search.get_code(row['city'])

data_manager.put_iata()

tomorrow = datetime.now() + timedelta(days=1)
plus_six = datetime.now() + timedelta(days=(6 * 30))


for city in sheet_data['prices']:
    flight = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY, 
        destination_city_code=city["iataCode"], 
        from_time=tomorrow,
        to_time=plus_six
    )
    if flight.price < city['lowestPrice']:
        notification.send_message(message=f"Low Price Alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}")
