from sensor_data import Sensor


class Message:
    """
    A randomly generated message that incorporates data from the Sense Hat. 
    """

    def __init__(self, greeting="Hello!", condition_intro="The conditions in my current room is ", conditions=""):
        """optionally takes a greeting and an intro to the conditions"""
        self.greeting = greeting
        self.condition_intro = condition_intro
        self.conditions = conditions

    def __repr__(self):
        """show representation of Message"""

        return f"<Message greeting='{self.greeting}' condition_intro ='{self.condition_intro}' self.conditions='{self.conditions}'>"

    def get_data(self):
        """get data from Sense Hat and CPU temp,
        and return CPU temp, sennsor temp, humidity, and air pressure."""

        sensor = Sensor()
        data = sensor.get_data()

        return data

    def set_rest(self):
        """calls to get data and sets the instance's rest of the message."""
        data = self.get_data()
        self.conditions = f"""{data['temperature']} F, {data['humidity']} % humidity, and the air pressure is {data['pressure']} mbar."""

    def get_message(self):
        """returns the message to be tweeted."""
        self.set_rest()
        message = f"{self.greeting} {self.condition_intro} {self.conditions}"
        return message
