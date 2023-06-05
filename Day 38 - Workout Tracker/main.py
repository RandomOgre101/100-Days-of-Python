import requests
from datetime import datetime

APP_ID = "APP_ID"
API_KEY = "API_KEY"

USERNAME = 'USERNAME'
PASSWORD = 'PASSWORD'

GENDER = "male"
WEIGHT_KG = 85
HEIGHT_CM = 190
AGE = 20


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/e44555c176f80a2a513f65568432fdf1/angelaWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

today = datetime.now().strftime("%Y/%m/%d")
time = datetime.now().strftime("%X")

r1 = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = r1.json()


for exercise in result["exercises"]:
    sheety_params = {
        'workout': {
            'date': today,
            'time': time,
            'exercise': exercise["name"].title(),
            'duration': exercise["duration_min"],
            'calories': exercise["nf_calories"],
        }
    }


r2 = requests.post(url=sheety_endpoint, json=sheety_params, auth=(USERNAME, PASSWORD))
print(r2.text)
