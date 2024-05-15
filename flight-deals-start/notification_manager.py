from twilio.rest import Client

account_sid = "ACabf380e9160a7b87d33c1d5b109053df"
auth_token = "2febc9aa2497ae7bbd96031c9215fc51"


class NotificationManager:
    def __init__(self):
        self.message = None
        self.client = None
        self.message_to_send = None

    def send_price_message(self, fare, departure_city, departure_iata, arrival_city, arrival_iata, departure_date,
                           arrival_date, stopover_city, total_stops):
        self.client = Client(account_sid, auth_token)

        self.message_to_send = f"Low price alert! Only £{fare} to fly from " \
                               f"{departure_city}-{departure_iata} to {arrival_city}-{arrival_iata}, from" \
                               f"{departure_date} to {arrival_date}.\n \n" \
                               f"The journey has {total_stops} stop over{stopover_city}"

        self.message = self.client.messages.create(body=self.message_to_send, from_="+447700101428", to="+447810136025")
        print(self.message.status)
