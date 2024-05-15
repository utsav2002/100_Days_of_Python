from data_manager import DataManager
from flight_search import FlightSearch

DataManager()  # Updates IATA code everytime
FlightSearch()  # Searches for a new deal and asks Notification Manager to send a mesage if found a new deal.
