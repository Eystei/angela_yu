import requests
import json
from datetime import datetime

MY_LAT = 40.179188
MY_LONG = 44.499104

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

# Beauty output in console
formatted_data = json.dumps(data, indent=2)
print(formatted_data + "\n")

sunrise = data["results"]["sunrise"]
sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
print(sunrise)

time_now = str(datetime.now())
print(f"hours from date_time_module: {time_now.split(' ')[1].split(':')[0]}")