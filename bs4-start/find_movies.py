import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movies_content = response.text

soup = BeautifulSoup(movies_content, 'html.parser')
soup.prettify()
# print(soup)

movie_list = soup.find_all(class_="listicleItem_listicle-item__title__BfenH", name="h3")
movie_list.reverse()
# print(movie_list)

titles = []
with open('movies.txt', 'w') as movie_file:
    for movie in movie_list:
        name_of_movie = str(movie.getText())
        movie_file.write(f"{name_of_movie}\n")
