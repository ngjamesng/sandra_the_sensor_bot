from os import getenv
from dotenv import load_dotenv
load_dotenv()

# twitter API keys
consumer_key = getenv("API_KEY")
consumer_secret = getenv("API_SECRET_KEY")
access_token = getenv("ACCESS_TOKEN")
access_token_secret = getenv("ACCESS_TOKEN_SECRET")

# Twilio API keys
twilio_account_sid = getenv("TWILIO_ACCOUNT_SID")
twilio_auth_token = getenv("TWILIO_AUTH_TOKEN")
twilio_phone_number = getenv("TWILIO_PHONE_NUMBER")
my_phone_number = getenv("MY_PHONE_NUMBER")