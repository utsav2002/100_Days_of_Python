# from datetime import datetime as dt, timedelta
import itertools
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = "ACabf380e9160a7b87d33c1d5b109053df"
auth_token = "2febc9aa2497ae7bbd96031c9215fc51"

stock_data_api_key = "O5S6U3VAO3QCAKRL"
stock_data_url = "https://www.alphavantage.co/query"
stock_data_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_data_api_key,
    "outputsize": "compact"
}

news_api_key = "26eb409ace354a3db0d9fb5202636cb8"
news_api_url = "https://newsapi.org/v2/everything"
news_api_parameters = {
    "qInTitle": COMPANY_NAME,
    "sort_by": "relevancy",
    "apiKey": news_api_key
}

## STEP 1: Use https://www.alphavantage.co

# today = dt.now().date()
# print(today)
# yesterday = today - timedelta(days=1)
# day_b4_yesterday = yesterday - timedelta(days=1)
#
# print(yesterday)

stock_data_response = (requests.get(url=stock_data_url, params=stock_data_parameters).json())["Time Series (Daily)"]
stock_data = dict(itertools.islice(stock_data_response.items(), 3))  # Data for today, yesterday and the day before

closing_price_yesterday = float(stock_data["2024-03-14"]["4. close"])
closing_price_day_b4_yesterday = float(stock_data["2024-03-13"]["4. close"])

percent_change = 7


def change_greater_than_5():
    global percent_change
    # percent_change = (
    #             ((closing_price_yesterday - closing_price_day_b4_yesterday) / closing_price_day_b4_yesterday) * 100)

    if abs(percent_change) >= 5:
        send_message()
    else:
        keep_checking = False


list_of_news_headlines = []
list_of_news_description = []
news_data = []


## STEP 2: Use https://newsapi.org
def get_news():
    global list_of_news_headlines, list_of_news_description, news_data

    news_data_response = requests.get(url=news_api_url, params=news_api_parameters).json()["articles"]

    # news_data = news_data_response[:3]

    # print(news_data)

    list_of_news_headlines = []
    # list_of_news_description = []

    for n in range(3):
        news_headline = news_data_response[n]["title"]
        list_of_news_headlines.append(news_headline)

    # news_description = news_data_response[n]["description"]
    # list_of_news_description.append(news_description)


## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
sign = None


def sign_to_show():
    global sign
    if percent_change > 0:
        sign = "🔺"
    else:
        sign = "🔻"
    return sign


def send_message():
    get_news()
    sign_to_show()

    client = Client(account_sid, auth_token)

    message_message = [f"{STOCK}: {sign}{round(percent_change)} \n" \
                       f"Headline: {article['title']}." for article in news_data]

    for messages in message_message:
        message = client.messages \
            .create(
            body=messages,
            from_="+447700101428",
            to="+447810136025"
        )
        print(message.status)

    # message_content = f"{STOCK}: {sign}{round(percent_change)} \n" \
    #                   f"" \
    #                   f"" \
    #                   f"" \
    #                   f"Headline: {list_of_news_headlines[0]}\n" \
    #                   f"Headline: {list_of_news_headlines[1]}\n" \
    #                   f"Headline: {list_of_news_headlines[2]}\n"


keep_checking = True

while keep_checking:
    change_greater_than_5()
