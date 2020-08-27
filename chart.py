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
        self.cpu_temp = [record['cpu_temp'] for record in self.json_data]
        self.room_temp = [record['room_temp'] for record in self.json_data]
        self.humidity = [record['humidity'] for record in self.json_data]
        self.air_pressure = [record['air_pressure']
                             for record in self.json_data]
        self.date = [record['date'] for record in self.json_data]

    def __repr__(self):
        """show representation of Chart"""

        return f"< Chart
        room_temp = '{self.room_temp}'
        humidity = '{self.humidity}'
        air_pressure = '{self.air_pressure}' >"

    def plot(self):
        """
        create a plot graph of the sensor data
        """
        plt.plot(self.date, self.room_temp, label="room temp")
        plt.plot(self.date, self.cpu_temp, label="cpu temp")
        plt.legend()
        plt.xlabel("date/time")
        plt.ylabel("Temperature(F)")
        plt.show()
