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

# get joke
BASE_URL = "https://official-joke-api.appspot.com/random_joke"

MAX_CHAR_COUNT = 280
api_call_limit = 10
joke = "x" * (MAX_CHAR_COUNT+1)

# prevent edge cases where jokes are too long and if so a new joke,
# or too many calls to the joke API
while(len(joke) > MAX_CHAR_COUNT and api_call_limit > 0):

    response = requests.get(BASE_URL)
    data = dict(response.json())
    # data == {"id":0,"type":"","setup":"","punchline":""}

    setup, punchline = [data.get(i) for i in ["setup", "punchline"]]

    joke = f"{setup} \n \n {punchline}"
    api_call_limit -= 1

# tweet the joke if valid
if len(joke) <= MAX_CHAR_COUNT:
    resp = twitter.update_status(status=joke)
    print("Tweeted: %s" % resp["text"])
else:
    # explicit for clarity
    None
