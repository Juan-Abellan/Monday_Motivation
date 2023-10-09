import smtplib
import datetime as dt
import random

my_email = "epictestemail@gmail.com"
my_password = "bqev iñpx vfny zooi"  # This password is an app password not the pw of the mail.

now = dt.datetime.now()
day_week = now.weekday()


if day_week == 0:
    with open(file="quotes.txt", mode="r") as motivational_quotes:
        quotes_list = [quote for quote in motivational_quotes.readlines()]
        chosen_quote = random.choice(quotes_list)
        print(chosen_quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection_sec = connection.starttls()
        connection_login = connection.login(user=my_email, password=my_password)
        connection_send = connection.sendmail(from_addr=my_email,
                                              to_addrs=my_email,
                                              msg=f"""Subject:Monday inspirational quote!\n\n{chosen_quote}"""
                                              )

