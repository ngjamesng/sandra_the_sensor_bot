from gpiozero import CPUTemperature
from sense_hat import SenseHat


class Sensor:
    """ A class to get sensor data"""

    def __init__(self, data={"temperature": "", "humidity": "", "pressure": ""}):
        """Make a new data dictionary for temperature, humidity, and pressure"""
        self.data = data

    def __repr__(self):
        """show representation of sensor data"""

        return f"<Sensor data='{self.data}'"

    def get_data(self):
        """
        Gets the temperature, humidity, & pressure. The measurement at the end is not included. 

        data = {
            "temperature": "73.5 F",
            "humidity": "50.2 %",
            "pressure": "1111 mbar"
        }
        """

        sense = SenseHat()

        temp = f"{self.get_sensor_temp(sense)}"
        humidity = f"{self.get_humidity(sense)}"
        pressure = f"{self.get_pressure(sense)}"

        data = {
            "temperature": temp,
            "humidity": humidity,
            "pressure": pressure
        }

        return data

    def C_TO_F(self, c):
        """
        Celsius to Fahrenheight conversion.
        """

        f = (c*9/5)+32
        return f

    def get_sensor_temp(self, sense):
        """
        returns the calibrated sensor temperature in Fahrenheit. For example, 70.5F.
        """

        # first, wake the sensors. The first reading is usually inaccurate.
        sense.get_temperature_from_pressure()
        sense.get_temperature_from_humidity()

        pressure_temp = sense.get_temperature_from_pressure()
        humidity_temp = sense.get_temperature_from_humidity()
        sense_temp = (pressure_temp + humidity_temp) / 2
        cpu_temp = CPUTemperature().temperature
        # convert values from Celsius to Fahrenheit
        sense_temp = self.C_TO_F(sense_temp)
        cpu_temp = self.C_TO_F(cpu_temp)

        FACTOR = 5.446
        calibrated_temp = sense_temp - ((cpu_temp - sense_temp)/FACTOR)
        calibrated_temp = round(calibrated_temp, 1)

        return calibrated_temp

    def get_humidity(self, sense):
        """returns the humidity. For example, 50.5%.
        """

        humidity = sense.get_humidity()
        humidity = round(humidity, 1)
        return humidity

    def get_pressure(self, sense):
        """ returns the air pressure in Millibars. For example, 1000 mbar"""
        pressure = sense.get_pressure()
        pressure = round(pressure, 1)
        return pressure
