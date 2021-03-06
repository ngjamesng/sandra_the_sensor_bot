from sensor_data import Sensor
from csv import DictWriter
from datetime import datetime
from os.path import isfile


def get_data():
    '''
    gets the data from the sensors, then add a date property.
    data = {
        "temperature": "73.5 F",
        "humidity": "50.2 %",
        "pressure": "1111 mbar",
        "date" : "dd/mm/YY H:M"
    }
    '''

    sense = Sensor()
    data = sense.get_data()
    data["date"] = datetime.now().strftime("%d/%m/%Y %H:%M")
    return data


def write_data(data):
    '''
    Takes in data and writes the result into a CSV file.
    If the CSV file already exists(has not yet been deleted),
    then just append data.
    Else, the file does not exist(has been deleted),
    then create a new file, write a headers and append the data.
    '''

    file_name = "data_log.csv"
    file_exists = isfile(f"./{file_name}")
    headers = ["temperature", "humidity", "pressure", "date"]

    if(file_exists):
        with open(file_name, "a") as csv_file:
            csv_writer = DictWriter(csv_file, fieldnames=headers)
            csv_writer.writerow(data)
    else:
        with open(file_name, "w") as csv_file:
            csv_writer = DictWriter(csv_file, fieldnames=headers)
            csv_writer.writeheader()
            csv_writer.writerow(data)


data = get_data()
write_data(data)
