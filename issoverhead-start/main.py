import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 54.974250  # Your latitude
MY_LONG = -1.618122  # Your longitude

my_email = "no.use.email.12344321@gmail.com"
password = "jyyobzcupehacrwy"


# Your position is within +5 or -5 degrees of the ISS position.

def close_or_not():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (abs(iss_longitude - MY_LAT) <= 5) and (abs(iss_longitude - MY_LONG)) < 5:
        return True


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:ISS LOOK UP NOTIFICATION \n\nPlease look up for ISS iin the sky.")

        connection.close()


def check_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if (time_now.hour > sunset) and ((time_now.hour % 24) < sunrise):
        return True


while check_dark():
    time.sleep(60)
    if close_or_not():
        send_email()
