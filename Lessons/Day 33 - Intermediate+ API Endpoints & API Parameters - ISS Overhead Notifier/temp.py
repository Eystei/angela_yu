import json
from datetime import datetime
import requests

MY_LATITUDE = "40.179188"
MY_LONGITUDE = "44.499104"

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": "0"
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
print(json.dumps(data, indent=2))

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now()


print(f"HOUR: {type(sunrise)} {sunrise=}")
print(f"HOUR: {type(sunset)} {sunset=}")
print(time_now.hour)

