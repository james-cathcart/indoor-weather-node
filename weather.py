import time
import math

class WeatherService:
    
    def __init__(self, sense_hat, location):
        self.sense = sense_hat
        self.location = location

    def get_data(self):
        
        raw_time = time.time()
        current_time = round(raw_time, None)

        humidity = round(self.sense.get_humidity(), None)
        pressure = self.sense.get_pressure()
        temperature = self.sense.get_temperature()
        
        data = {"time": current_time, "humidity": humidity, "temperature": temperature, "pressure": pressure, "location": self.location}
        
        return data
