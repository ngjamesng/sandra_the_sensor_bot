from datetime import date
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
import requests


twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# get fact for today
BASE_URL = "http://numbersapi.com/"
today = date.today().strftime("%m/%d")
response = requests.get(f"{BASE_URL}{today}/date")
fact = response.text

# tweet the fact
resp = twitter.update_status(status=fact)
print("Tweeted: %s" % resp["text"])