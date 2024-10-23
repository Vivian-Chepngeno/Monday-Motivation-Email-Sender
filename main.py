import smtplib
import datetime as dt
import random

my_email = "chepngenovivian55@gmail.com"
password = "wins bmzu pscn ppyl"

# Get the current date and time
now = dt.datetime.now()
weekday = now.weekday()

# Check if today is Monday (weekday == 0 for Monday)
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=password)  # Log in

        # Send the email with a subject and the quote
        connection.sendmail(
            from_addr=my_email,
            to_addrs="chebwogenbi@gmail.com",
            msg=f"Subject: Monday Motivation\n\n{quote}"  # f-string to insert the quote
        )

    print("Email sent successfully!")
