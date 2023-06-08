import requests
from datetime import datetime, timedelta

<<<<<<< HEAD
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
=======
TEQUILA_ENDPOINT = ""
>>>>>>> fb909f0c579e4a084718d83cee4db9ab2f73b9d7
TEQUILA_KEY = ""


class FlightData:
    
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
