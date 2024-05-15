import requests


class DataManager:

    def __init__(self):
        self.city_list = ["Paris", "Berlin", "Tokyo"]
        self.iata_codes = []
        self.price_list = []

        self.KIWI_API_KEY = "s9zlRjORwe0LX9-YxE2-XwoHR-iW2wJB"
        self.sheety_url = "https://api.sheety.co/543cb269cae665b967c180408dfe5c22/flightDeals/prices"
        self.sheety_response = (requests.get(self.sheety_url)).json()

        # Make list of the cities mentioned
        for response in self.sheety_response["prices"]:
            self.city_list.append(response["city"])
            self.iata_codes.append(response["IATA Code"])
            self.price_list.append(response["Lowest Price"])

        kiwi_headers = {
            "apikey": self.KIWI_API_KEY,
        }

        for city in self.city_list:
            self.kiwi_url = f"https://api.tequila.kiwi.com/locations/query/?term={city}" \
                            f"&locale=en-US&location_types=airport&limit=10&active_only=true"
            self.kiwi_response = (requests.get(self.kiwi_url, headers=kiwi_headers)).json()
            city_iata = self.kiwi_response["locations"][0]["city"]["code"]
            self.iata_codes.append(city_iata)

            self.sheety_url = f"https://api.sheety.co/543cb269cae665b967c180408dfe5c22/flightDeals/prices/" \
                              f"{(self.city_list.index(city)) + 2}"
            data_to_put = {
                "price": {
                    "iataCode": city_iata
                }
            }

            requests.put(self.sheety_url, json=data_to_put)

    def update_lowest_price(self, fare, city_to_index):
        self.sheety_url = f"https://api.sheety.co/543cb269cae665b967c180408dfe5c22/flightDeals/prices/" \
                          f"{city_to_index + 2}"
        data_to_put = {
            "price": {
                "lowestPrice": fare
            }
        }

        requests.put(self.sheety_url, json=data_to_put)
