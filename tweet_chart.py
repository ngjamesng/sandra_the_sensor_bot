from twython import Twython
from csv import DictReader
from chart import Chart


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

def tweet_chart_image(img_file_name = "chart.png"):
    """
    Create the chart image, and then tweet the image.
    """
    data = None
    csv_file_name = "data_log.csv"

    
    with open(csv_file_name, "r") as file:
        csv_reader = DictReader(file)
        data = list(csv_reader)
        
    chart = Chart(data)
    chart.plot_and_create_image(img_file_name)
    
    with open(img_file_name, "rb") as image:
        response_1 = twitter.upload_media(media=image)
        response_2 = twitter.update_status(status="Here's a chart of my data!", media_ids=[response_1["media_id"]])
        print("Tweeted: %s" % response_2["text"])
        
tweet_chart_image()