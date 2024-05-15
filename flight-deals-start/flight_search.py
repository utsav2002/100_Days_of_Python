import requests
import datetime as dt

from data_manager import DataManager
from notification_manager import NotificationManager

data_manager = DataManager()
notification_manager = NotificationManager()

KIWI_API_KEY = "s9zlRjORwe0LX9-YxE2-XwoHR-iW2wJB"


class FlightSearch:

    def __init__(self):
        # Search for flight
        self.tomorrow = (dt.date.today() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
        self.six_months_later_date = (dt.date.today() + dt.timedelta(weeks=26)).strftime("%d/%m/%Y")

        self.search_header = {
            "apikey": KIWI_API_KEY,
        }

        for city_iata in data_manager.iata_codes:
            self.kiwi_search_url = f"https://api.tequila.kiwi.com/v2/search?fly_from=London&fly_to={city_iata}" \
                                   f"&date_from={self.tomorrow}&date_to={self.six_months_later_date}&curr=GBP&limit=1"

            self.response = (requests.get(url=self.kiwi_search_url, headers=self.search_header).json())["data"][0]
            print(self.response)

            flying_from = self.response["cityFrom"]
            flying_from_iata = self.response["flyFrom"]
            flying_to = self.response["cityTo"]
            flying_to_iata = self.response["flyTo"]
            depart_date = (self.response["local_departure"]).strftime("%Y-%m-%d")
            arrive_date = (self.response["local_arrival"]).strftime("%Y-%m-%d")
            journey_price = self.response["price"]
            stop_over_city = "."
            no_of_stops = "0"

            if len(self.response["route"]) == 2:
                stop_over_city = f" via {self.response['route']['0']['cityTo']}."
                no_of_stops = "1"

            index_of_city = data_manager.city_list.index(city_iata)
            # Check if the price is less
            if int(journey_price) < int(data_manager.price_list[index_of_city]):
                data_manager.update_lowest_price(fare=journey_price, city_to_index=index_of_city)
                notification_manager.send_price_message(fare=journey_price,
                                                        departure_city=flying_from, departure_iata=flying_from_iata,
                                                        arrival_city=flying_to, arrival_iata=flying_to_iata,
                                                        departure_date=depart_date, arrival_date=arrive_date,
                                                        stopover_city=stop_over_city, total_stops=no_of_stops)

            print("Found a new deal and sent message!")
