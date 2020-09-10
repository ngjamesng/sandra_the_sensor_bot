from sensor_data import Sensor
from csv import DictWriter
from datetime import datetime


def get_data():
    '''
    gets the data from the sensors. 
    data = {
        "temperature": "",
        "humidity": "",
        "pressure": ""
        "date" : ""
    }
    '''

    sensor = Sensor()
    data = sensor.get_data()
    data["date"] = datetime.now().strftime("%d/%m/%Y %H:%M")
    print("data", data)
    return data


def write_data(data):
    """
    Takes in data and writes the results into a CSV file. 
    """
    file_name = "data_log.csv"
    data = get_data()
    with open(file_name, "W") as csv_file:
        headers = ["temp", "humidity", "pressure", "date"]
        csv_writer = DictWriter(csv_file, fieldnames=headers)


get_data()
