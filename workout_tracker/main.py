import requests
from datetime import datetime as dt
import stringify as stringify

APP_ID = "24a52d82"
API_KEY = "7e3454d70cee33917ff75cdb8f79721a"

GENDER = "Male"
AGE = "21"
WEIGHT = "75"

nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_parameters = {
    "query": (input("What exercise did you do?: ")),
    # "Gender": GENDER,
    # "Age": AGE,
    # "Weight": WEIGHT
}

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = (requests.post(url=nutritionix_url, json=nutritionix_parameters, headers=nutritionix_headers)).json()
print(response)

today_date = (dt.now()).strftime("%d/%m/%Y")
today_time = (dt.now()).strftime("%H:%M:%S")

sheety_url = "https://api.sheety.co/543cb269cae665b967c180408dfe5c22/utsavMyWorkouts/workouts"

for (exercise) in response["exercises"]:

    exercise_name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]

    print(exercise_name, duration, calories)

    sheety_parameters = {
        "workout": {
            "Date": today_date,
            "Time": today_time,
            "Exercise": exercise_name,
            "Duration": duration,
            "Calories": calories
        }
    }

    sheety_response = (requests.post(url=sheety_url, json=sheety_parameters))
    print(sheety_response.text)
