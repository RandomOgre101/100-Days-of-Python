import smtplib
import datetime as dt
import random

# my_email = "email"
# password = "password"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="daxsteel1234@gmail.com", msg="Subject: Hello World!\n\nThis is the body.")


# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()
# print(day_of_week)
# date_of_birth = dt.datetime(year=)


with open("quotes.txt") as file:
    quotes = file.read().splitlines()

quote = random.choice(quotes)
print(quote)
now = dt.datetime.now()
day_of_week = now.weekday()

my_email = "email"
password = "password"

if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="TO_ADDRESS", msg=f"Subject: Motivational Quote\n\n{quote}")