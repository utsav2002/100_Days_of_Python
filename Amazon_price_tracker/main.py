import requests
from bs4 import BeautifulSoup
import smtplib
import lxml

AMAZON_URL = "https://www.amazon.co.uk/Wrangler-Authentics-Classic-Relaxed-Stonewash/dp/B00XKXTVCC/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=8z10e&content-id=amzn1.sym.6aea875e-359f-49f3-864f-cff62d586b6a%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=6aea875e-359f-49f3-864f-cff62d586b6a&pf_rd_r=DW1GA9VWCN01PHFGVKYW&pd_rd_wg=xBYBo&pd_rd_r=4890c02a-d332-4434-8c59-5aa1c8b43472&pd_rd_i=B00XKXTVCC"
AMAZON_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
}

EMAIL = "no.use.email.12344321@gmail.com"
PASS = "jyyobzcupehacrwy"
receiver_email = "utsavkothari2002@gmail.com"

response = requests.get(AMAZON_URL, headers=AMAZON_HEADERS)
soup = BeautifulSoup(response.content, "lxml")

price_of_product = float((soup.find(name="span", class_="a-offscreen").getText()).split("£")[1])
print(price_of_product)


def send_email(price):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASS)
        connection.sendmail(from_addr=EMAIL, to_addrs=receiver_email,
                            msg=f"Price is £{price} now.")

        connection.close()


if price_of_product < 30:
    send_email(price=price_of_product)
