import requests
from twilio.rest import Client

account_sid = "ACabf380e9160a7b87d33c1d5b109053df"
auth_token = "2febc9aa2497ae7bbd96031c9215fc51"

client = Client(account_sid, auth_token)


end_point = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "82fbed8a8b7f1cbe7d657dd4a114d874"

parameters = {
    "lat": 54.974225,
    "lon": -1.618103,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=end_point, params=parameters)
response.raise_for_status()

final_data = (response.json())["list"]

first_hour_id = final_data[0]["weather"][0]["id"]

it_will_rain = False

for hours in range(4):
    condition_data = (final_data[hours]["weather"][0]["id"])
    if hours < 700:
        it_will_rain = True

if it_will_rain:
    print("Bring an Umbrella.")

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_="+447700101428",
                     to="+447810136025"
                 )
print(message.status)
