from twython import Twython
from message import Message

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

message = "Hello world!"
twitter.update_status(status=message)
print("Tweeted: %s" % message)