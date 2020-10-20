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
payload = {"json": ""}
today = date.today().strftime("%m/%d")

MAX_CHAR_COUNT = 280
api_call_count = 0
fact = "x" * (MAX_CHAR_COUNT+1)

# prevent edge cases where facts are too long
# or too many calls to the fact API
while(len(fact) > MAX_CHAR_COUNT and api_call_count < 10):

    response = requests.get(f"{BASE_URL}{today}/date", params=payload)
    # response == http://numbersapi.com/10/19/date?json=

    data = dict(response.json())
    fact = data.get("text")
    api_call_count += 1

# tweet the fact if valid
if len(fact) <= MAX_CHAR_COUNT:
    resp = twitter.update_status(status=fact)
    print("Tweeted: %s" % resp["text"])
else:
    # explicit for clarity
    None