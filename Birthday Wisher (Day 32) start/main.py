import random
import smtplib
import datetime as dt

my_email = "no.use.email.12344321@gmail.com"
password = "jyyobzcupehacrwy"

receiver_email = "anvithavallamsetty2003@gmail.com"

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_the_week = now.weekday()
#
# print(day_of_the_week)

now = dt.datetime.now()

# print(quotes_list)

today = now.weekday()
# print(today)

keep_wishing = True

while keep_wishing:
    if today == 3:
        with open('quotes.txt', 'r') as quotes:
            quotes_list = quotes.readlines()
            random_quote = random.choice(quotes_list)

            print(random_quote)

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=receiver_email,
                                    msg=f"Subject:HAHA! You have been pranked!! \n\n{random_quote}")

                connection.close()
