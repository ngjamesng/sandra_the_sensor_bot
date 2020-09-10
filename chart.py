import matplotlib.pyplot as plt
from dateutil import parser


class Chart:
    """
    A chart based on the data that is in the text file.
    """

    def __init__(self, data):
        """
        Opens a CSV file, reads the data and sets the data.
        """
        self.data = data
        self.temperature = [float(record.get('temperature')) for record in self.data]
        self.humidity = [float(record.get('humidity')) for record in self.data]
        self.pressure = [float(record.get('pressure')) for record in self.data]
        self.date = [record.get('date') for record in self.data]

    def __repr__(self):
        """show representation of Chart"""

        return f"< Chart temperature = '{self.temperature}' humidity = '{self.humidity}' air_pressure = '{self.pressure}' >"


    def plot_and_create_image(self, image_name="chart.png"):
        """
        create a plot graph of the sensor data.
        """
        
        fig, temperature_line = plt.subplots()
        
        temperature_color = "tab:red"
        temperature_line.set_xlabel("date & time")
        temperature_line.set_ylabel("Temperature (F)", color=temperature_color)
        temperature_line.plot(self.date, self.temperature, color=temperature_color)
        temperature_line.tick_params(axis='y', labelcolor=temperature_color)
        
        humidity_line = temperature_line.twinx()
        
        humidity_color = "tab:blue"
        humidity_line.set_ylabel("humidity (%)", color=humidity_color)
        humidity_line.plot(self.date, self.humidity, color=humidity_color)
        humidity_line.tick_params(axis='y', labelcolor=humidity_color)
        
        
        fig.tight_layout()
        plt.savefig(image_name)
