from sensor_data import Sensor
from csv import DictWriter
from datetime import datetime


def get_data():
    '''
    gets the data from the sensors. 
    data = {
        "temperature": "73.5 F",
        "humidity": "50.2 %",
        "pressure": "1111 mbar"
        "date" : "dd/mm/YY H:M"
    }
    '''

    sensor = Sensor()
    data = sensor.get_data()
    data["date"] = datetime.now().strftime("%d/%m/%Y %H:%M")
    return data


def write_data(data):
    """
    Takes in data and writes the result into a CSV file. 
    """
    file_name = "data_log.csv"
    data = get_data()
    with open(file_name, "W") as csv_file:
        headers = ["temperature", "humidity", "pressure", "date"]
        csv_writer = DictWriter(csv_file, fieldnames=headers)
        csv_writer.writerow(data)


data = get_data()
write_data(data)
