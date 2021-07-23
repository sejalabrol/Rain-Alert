import os
from dotenv import load_dotenv
from twilio.rest import Client
import requests

"""
# for python anywhere + twilio
# https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/
from twilio.http.http_client import TwilioHttpClient
"""

load_dotenv()
OWP_API_KEY = os.getenv("OWP_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
LATITUDE, LONGITUDE = os.getenv("LATITUDE"), os.getenv("LONGITUDE")
SENDERS_NUMBER = os.getenv("SENDERS_NUMBER")
RECEIVERS_NUMBER = os.getenv("RECEIVERS_NUMBER")

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": OWP_API_KEY,
    "exclude": "daily,current,minutely",
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall", params=parameters
)
response.raise_for_status()
weather_data = response.json()

# Task - to print 'Take an Umbrella' if it is going to rain in the next twelve hours
twelve_hour_data = weather_data["hourly"][:12]  # list of twelve dictionaries

will_rain = False
for _ in twelve_hour_data:
    id = _["weather"][0]["id"]
    if id < 700:
        will_rain = True

if will_rain:
    """
    #for python anywhere + twilio
    # https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, http_client=proxy_client)
    """
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body="It's going to rain, take an umbrella☂️",
        from_=SENDERS_NUMBER,
        to=RECEIVERS_NUMBER,
    )
    print(message.status)
