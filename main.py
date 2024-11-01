import datetime as dt
import random
import smtplib

import pandas as pd

df = pd.read_csv("birthdays.csv")
now = dt.datetime.now()

letters_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
random_letter = random.choice(letters_list)

my_email = "ENTER YOUR EMAIL ID HERE"
password = "ENTER YOUR PASSWORD HERE"

for x in range(len(df)):
    if df["month"].iloc[x] == now.month and df["day"].iloc[x] == now.day:
        name = df["name"].iloc[x]
        birthday_email = df["email"].iloc[x]
        placeholder = "[NAME]"

        with open(f"letter_templates/{random_letter}", "r") as letter:
            content = letter.read()
            content = content.replace(placeholder, name)

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday_email,
                msg=f"Subject: Happy Birthday!\n\n{content}"
            )
