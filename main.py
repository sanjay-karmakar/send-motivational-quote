import datetime as dt
import smtplib
import random

FROM_EMAIL="sanjaykarmakar86@gmail.com"
PASSWORD="ljhoiddkvqialcyh"

now = dt.datetime.now()
weekday=now.weekday()

if weekday == 3:
    try:
        with open("quotes.txt", mode="r", encoding="utf-8") as quotes_file:
            all_quotes = quotes_file.read().splitlines()
            quote = random.choice(all_quotes)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=FROM_EMAIL, password=PASSWORD)

            message = f"Subject: Thursday Motivation\n\n{quote}".encode("utf-8")

            connection.sendmail(
                from_addr=FROM_EMAIL,
                to_addrs="100websolution@gmail.com",
                msg=message
            )
            print("Motivational email sent successfully!")

    except FileNotFoundError:
        print("Error: quotes.txt was not found in the project folder.")

    except smtplib.SMTPAuthenticationError:
        print("Error: Check your email or App Password.")