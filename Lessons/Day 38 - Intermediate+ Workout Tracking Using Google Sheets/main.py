import requests
import os
from datetime import datetime

GENDER = "male"
WEIGHT_KG = "97.7"
HEIGHT_CM = "185"
AGE = "32"

NUTRIONIX_APP_ID = os.environ.get("NUTRIONIX_APP_ID")
NUTRIONIX_API_KEY = os.environ.get("NUTRIONIX_API_KEY")
MAIN_URL = "https://trackapi.nutritionix.com"
HEADERS = {
    "x-app-id": NUTRIONIX_APP_ID,
    "x-app-key": NUTRIONIX_API_KEY,
}

# EXERCISE_ENDPOINTS
EXERCISE_ENDPOINT = f"{MAIN_URL}/v2/natural/exercise"
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")

exercise_txt = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_txt,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=EXERCISE_ENDPOINT, headers=HEADERS, json=parameters)
result = response.json()
print(result)

# SHEETY_ENDPOINTS
today_date = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")
bearer_headers = {
    "Authorization": f"Bearer {os.environ.get('BEARER_SHEETY')}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "list_1": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.text)
