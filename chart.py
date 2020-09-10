import matplotlib.pyplot as plt
from dateutil import parser


class Chart:
    """
    A chart based on the data that is in the text file.
    """

    def __init__(self, json_data):
        """
        takes in JSON data and creates a chart
        """
        self.json_data = json_data
        self.temperature = [record['temperature'] for record in self.json_data]
        self.humidity = [record['humidity'] for record in self.json_data]
        self.pressure = [record['pressure'] for record in self.json_data]
        self.date = [record['date'] for record in self.json_data]

    def __repr__(self):
        """show representation of Chart"""

        return f"< Chart temperature = '{self.temperature}' humidity = '{self.humidity}' air_pressure = '{self.pressure}' >"

    def plot(self):
        """
        create a plot graph of the sensor data
        """
        plt.plot(self.date, self.temperature, label="room temp")
        plt.plot(self.date, self.humidity, label="humidity")
        plt.legend()
        plt.xlabel("date/time")
        plt.ylabel("Temperature(F)")
        plt.show()



