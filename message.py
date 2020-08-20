class Message:
    """
    A randomly generated message that incorporates data from the Sense Hat. 
    """
    
    def __init__(self, output=""):
        """Make a new string, starting with an empty string."""
        
        self.output = output
        
    def __repr__(self):
        """show representation of Message"""
        
        return f"<Message output='{self.output}'"
    
    def C_TO_F(self, c):
        f = (c*9/5)+32
        return f
    
    def get_sensor_temp(self, sense):
        """
        returns the calibrated sensor temperature in Fahrenheit. For example, 70.5F
        """
        from gpiozero import CPUTemperature
        
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
        
        return f"{calibrated_temp}F"
    
    def get_humidity(self, sense):
        humidity = sense.get_humidity()
        humidity = round(humidity, 1)        
        return f"{humidity}%"
        
    def get_air_pressure(self, sense):
        

    def get_data(self):
        """get data from Sense Hat and CPU temp,
        and return CPU temp, sennsor temp, humidity, and air pressure."""
        
        from sense_hat import SenseHat
        
        sense = SenseHat()
        
        temp = self.get_sensor_temp(sense)
        humidity = self.get_humidity(sense)
        
        
        data = {
            "temperature": temp,
            "humidity" :humidity
        }
        
        return data
        