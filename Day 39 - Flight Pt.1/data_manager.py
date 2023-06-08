import requests
from pprint import pprint

SHEETY_ENDPOINT = ""


class DataManager:
    def __init__ (self):
        self.data = {}

    def get_sheety(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        self.data = response.json()
        return self.data


    def put_iata(self):
        for city in self.data['prices']:
            updated = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=updated)
