import requests
import smtplib, ssl
import os
from send_email import send_email

topic = "tesla"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&from=2024-03-05&"
       "sortBy=publishedAt&apiKey="
       "d395f29510bf401bb6e65148ae903558&language=en")

# Get API
request = requests.get(url)
# Convert API into a python dictionary (JSON)
content = request.json()
message = "Subject: Today's News \n"

for article in content['articles'][:20]:
    if article["title"] is not None and article["description"] is not None:
        message = message + article["title"] + "\n" \
                   + article["description"] + "\n" \
                   + article["url"] + 2*"\n"

message = message.encode("utf-8")
send_email(message)
