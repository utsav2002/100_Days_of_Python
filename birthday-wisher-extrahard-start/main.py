import smtplib
import datetime as dt
import random
import pandas as pd

my_email = "no.use.email.12344321@gmail.com"
password = "jyyobzcupehacrwy"

# Today's details
now = dt.datetime.now()

today_date = now.day
today_month = now.month


def is_it_birthday(date, month):
    if (date == today_date) and (month == today_month):
        return True


# import birthdays
with open('birthdays.csv', 'r') as birthdays:
    birthdays_data = pd.read_csv(birthdays)

# Go through all the birthdays
for index, row in birthdays_data.iterrows():

    birthday_date = row["day"]
    birthday_month = row["month"]
    birthday_name = row["name"]
    birthday_email = row["email"]

    if is_it_birthday(date=birthday_date, month=birthday_month):
        random_letter = random.randint(1, 3)

        letter = (open(f"letter_templates/letter_{random_letter}.txt")).read()

        # Update the name
        letter = letter.replace("[NAME]", birthday_name)

        # Send an email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=birthday_email,
                                msg=f"Subject:Happy Birthday! \n\n{letter}")

            connection.close()
