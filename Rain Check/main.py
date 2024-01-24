import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "86a22b8a3a4c8f3c9416d86eb187c15a"
ACC_ID = "AC3dc4d93f088d7b8b4bf6b492ccce8475"
AUTH_TOKEN = "467daacbb54acff3014511076b1aea58"

weather_params = {
    "lat": 53.726669,
    "lon": -127.647621,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
data = response.json()

will_rain = False

for hr_data in data['list']:
    condition = hr_data['weather'][0]['id']
    if condition < 700:
        will_rain = True

if will_rain:
    client = Client(ACC_ID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="It's going to rain today. Bring an umbrella.",
        from_='+18333563915',
        to='+15054596727'
    )

    print(message.status)