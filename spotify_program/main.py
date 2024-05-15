import requests
from bs4 import BeautifulSoup

SPOTIFY_CLIENT_ID = "0adf6cc526714f98989c8e46c16be1d9"


user_input = input("What date do you eant to travel to? Type the date in this format: YYYY-MM-DD: ")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{user_input}/")

soup = BeautifulSoup(response.text, 'html.parser')

song_list = soup.select("li ul li h3")
song_names_list = [song.getText().strip() for song in song_list]
print(song_names_list)


