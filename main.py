
from smtplib import SMTP
import datetime as dt
from random import choice

now = dt.datetime.now()
current_weekday = now.weekday()
# 5 is Saturday
if current_weekday:
    # Open file with path ("path/to/file")
    with open("quotes.txt") as q:
        quotes = q.readlines()
        chosen_quotes = choice(quotes)

    # Set up your Email

    # This is my clone Email :)
    my_email= "ngoc2002quach@gmail.com"
    # My password was created randomly by my
    # previous Project called "Password Manager"
    password = "99!+h0$TPkG&7ZpQ"

    # Let's connect them

    # I recommend you to turn off your security
    # and allow less security app in Gmail settings

    with SMTP("smtp.gmail.com") as connection:
        # connection secure
        connection.starttls()
        # Login
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ngoc2002quach@gmail.com",
            msg="Subject:Motivate Quotes\n\n" + f"{chosen_quotes}"
        )

    # Done!!
    # Let's run them 


