import time
import math

class WeatherService:
    
    def __init__(self, sense_hat, location):
        self.sense = sense_hat
        self.location = location

    def get_data(self):

        formatted_time = time.strftime('%Y-%m-%dT%H:%M:%SZ')

        humidity = round(self.sense.get_humidity(), None)
        pressure = self.sense.get_pressure()
        temperature = self.sense.get_temperature()
        
        data = {"timestamp": formatted_time, "humidity": humidity, "temperature": temperature, "pressure": pressure, "location": self.location}
        
        return data
