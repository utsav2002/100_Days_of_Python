from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
articles = soup.find_all(name='span', class_='titleline')

article_texts = []
article_links = []

for article_tag in articles:
    article_text = article_tag.getText()
    print(article_text)
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvotes = [score.getText().split()[0] for score in soup.find_all(name="upvote", class_="votearrow")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

# highest_upvote = max(article_upvotes)
# index_of_highest_upvote = article_upvotes.index(highest_upvote)

# most_upvote_article = article_texts[index_of_highest_upvote]
# most_upvote_article_link = article_links[index_of_highest_upvote]

# print(f"{most_upvote_article}, {most_upvote_article_link}, with {highest_upvote} votes.")





# html_file = open('website.html', 'r')
# content = html_file.read()
#
# soup = BeautifulSoup(content, 'html.parser')
# # print(soup.prettify())
# print(soup.title)
# print(soup.title.string)
#
#
# print(soup.find_all(name="h3")) # Prints all h3s
# print(soup.select_one(selector="h3")) # Prints the first h3
