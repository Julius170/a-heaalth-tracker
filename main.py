import os
import requests
from datetime import datetime
APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ['APP_KEY']
EXERCISE_ENDPOINT = os.environ['EXERCISE_ENDPOINT']
SHEETY_URL = os.environ['sheety_url']
SHEETY_TOKEN = os.environ['SHEETY_TOKEN']
print(APP_ID, APP_KEY, EXERCISE_ENDPOINT, SHEETY_TOKEN, SHEETY_URL)


user_data= input("Tell me what exercise you did? ")


GENDER = "Male"
YOUR_AGE = "30"
YOUR_HEIGHT = "50"
YOUR_WEIGHT = "90"

today = datetime.now()


params= {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

body = {
    "query": user_data,
    "gender":GENDER,
    "weight_kg":YOUR_WEIGHT,
    "height_cm":YOUR_HEIGHT,
    "age":YOUR_AGE,
}

response = requests.post(url=EXERCISE_ENDPOINT, json=body, headers=params)
routine = (response.json())
print(routine)

exercise = (routine["exercises"][0]["user_input"])
duration = (int(routine["exercises"][0]["duration_min"]))
calories = (int(routine["exercises"][0]["nf_calories"]))


header = {
    "Authorization": SHEETY_TOKEN,
    "Content-Type": "application/json",
}

updates = {
    "workout":{
    "date": today.strftime("%Y%m%d"),
    "time": today.strftime("%H:%M:%S"),
    "exercise": exercise,
    "duration": duration,
    "calories": calories,
}
}
 
response2 = requests.post(url=SHEETY_URL, json=updates, headers=header)
print(response2.raise_for_status())
print(response2.json())

