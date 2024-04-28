import requests
from twilio.rest import Client
import os

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWN_API_KEY")
account_sid = "s56fdg38576ds8h8sdf4567sd95fsdf768sd4fg6"
auth_token = os.environ.get("AUTH_TOKEN")
"http://api.openweathermap.org/data/2.5/weather?q=Yerevan&appid=3c8ca9c2ad9e804db9440f473b35f8aa"

weather_params = {
    "lat": "40.179188",
    "lon": "44.499104",
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+8762493872843",
        to="+96428795644738"
    )
    print(message.status)