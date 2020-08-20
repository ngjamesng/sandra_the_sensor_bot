from twython import Twython
from message import Message
from sensor_data import Sensor

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

m = Message()
message = m.get_message()
twitter.update_status(status=message)
print("Tweeted: %s" % message)