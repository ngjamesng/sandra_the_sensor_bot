from sensor_data import Sensor
from csv import DictWriter

def get_data():
    """
    gets the data from the sensors. 
    """

    sensor = Sensor()
    data = sensor.get_data()
    temp = data.temperature
    humidity = data.humidity
    pressure = data.pressure

    print("temp!", temp)


def write_data(data):
    """
    Takes in data and writes the results into a CSV file. 
    """

get_data()