import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from dateutil import parser
from datetime import datetime


class Chart:
    """
    A chart based on the data that is in the text file.
    """

    def __init__(self, data):
        """
        Opens a CSV file, reads the data and sets the data.
        """
        self.data = data
        self.temperature = [float(record.get('temperature'))
                            for record in self.data]
        self.humidity = [float(record.get('humidity')) for record in self.data]
        self.pressure = [float(record.get('pressure')) for record in self.data]
#         self.date = [parser.parse(record.get('date'), dayfirst=True) for record in self.data]
        self.date = [datetime.strptime(record.get(
            'date'), "%d/%m/%Y %H:%M") for record in self.data]

    def __repr__(self):
        """show representation of Chart"""

        return f"< Chart temperature = '{self.temperature}' humidity = '{self.humidity}' air_pressure = '{self.pressure}' >"

    def plot_and_create_image(self, image_name="chart.png"):
        """
        create a plot graph of the sensor data, with two data points, ax1 and ax2.
        """

        # ax1 is for temperature for the ylabel and date for the xlabel.
        fig, ax1 = plt.subplots()

        temp_color = "tab:red"
        ax1.set_xlabel("Date & Time")
        ax1.set_ylabel("Temperature (F)", color=temp_color)
        ax1.plot(self.date, self.temperature, color=temp_color)
        ax1.tick_params(axis='y', labelcolor=temp_color)
        ax1.set_xticklabels(self.date, rotation=90)
        ax1.grid(True)

        # ax2 is for the humidity. We don't set the xlabel because ax1 already has the date.
        ax2 = ax1.twinx()

        hum_color = "tab:blue"
        ax2.set_ylabel("humidity (%)", color=hum_color)
        ax2.plot(self.date, self.humidity, color=hum_color)
        ax2.tick_params(axis='y', labelcolor=hum_color)

        fig.tight_layout()
        fig.autofmt_xdate()
        plt.savefig(image_name)
