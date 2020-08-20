from os import getenv
from dotenv import load_dotenv
load_dotenv()

consumer_key = getenv("API_KEY")
consumer_secret = getenv("API_SECRET_KEY")
access_token = getenv("ACCESS_TOKEN")
access_token_secret = getenv("ACCESS_TOKEN_SECRET")
