import time
import math

class WeatherService:
    
    def __init__(self, sense_hat, location):
        self.sense = sense_hat
        self.location = location

    def get_data(self):
        
        raw_time = time.time()
        formattedTime =  time.strftime('%Y-%m-%dT%H:%M:%SZ')
        print(f'timestamp: {formattedTime}')

        humidity = round(self.sense.get_humidity(), None)
        pressure = self.sense.get_pressure()
        temperature = self.sense.get_temperature()
        
        data = {"time": formattedTime, "humidity": humidity, "temperature": temperature, "pressure": pressure, "location": self.location}
        
        return data
