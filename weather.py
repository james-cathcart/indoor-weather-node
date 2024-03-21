from datetime import datetime

def convert_to_fahrenheit(celsius_temp):
    return (celsius_temp * (9/5)) + 32


class WeatherService:
    
    def __init__(self, sense_hat, location, cardinal_direction, floor):
        self.sense = sense_hat
        self.location = location
        self.cardinal_direction = cardinal_direction
        self.floor = floor

    def get_data(self):

        formatted_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

        humidity = round(self.sense.get_humidity(), None)
        pressure = self.sense.get_pressure()
        temperature = self.sense.get_temperature()
        
        data = {
            "_timestamp": formatted_time,
            "humidity": humidity,
            "temperature": temperature,
            "temperature_f": convert_to_fahrenheit(temperature),
            "pressure": pressure,
            "location": self.location,
            "cardinal_direction": self.cardinal_direction,
            "floor": self.floor
        }

        print(f'collected data: {data}')

        return data
