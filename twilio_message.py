from twilio.rest import Client
from message import Message

from auth import (
    twilio_account_sid,
    twilio_auth_token,
    twilio_phone_number,
    my_phone_number
)
account_sid = twilio_account_sid
auth_token = twilio_auth_token
client = Client(account_sid, auth_token)

m = Message()
message = m.get_message()

twilio_text = client.messages.create(
    body=message,
    from_=twilio_phone_number,
    to=my_phone_number
)

print(twilio_text.sid)
