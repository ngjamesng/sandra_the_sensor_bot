from twilio.rest import Client

from auth import (
    twilio_account_sid,
    twilio_auth_token,
    twilio_phone_number,
    my_phone_number
)

client = Client(account_sid=twilio_account_sid, auth_token=twilio_auth_token)

message = client.messages.create(
    body="testing!",
    from_=twilio_phone_number,
    to=my_phone_number
)

print(message.sid)
