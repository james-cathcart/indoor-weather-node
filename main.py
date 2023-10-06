from sense_hat import SenseHat
import time
from weather import WeatherService
from master import MasterService
import os

read_interval_seconds = 60
sense = SenseHat()

green = (0, 255, 0)
white = (255, 255, 255)

master_host = os.getenv('MASTER_HOST')
master_port = os.getenv('MASTER_PORT')
location = os.getenv('WEATHER_LOCATION')

def main():

    if master_host is None or master_host == '':
        exit(1)
    elif master_port is None or master_port == '':
        exit(2)
    elif location is None or location == '':
        exit(3)

    weather_svc = WeatherService(sense, location)
    master_svc = MasterService(master_host, master_port)
    print('starting weather node')

    while True:
        data = weather_svc.get_data()
        master_svc.record_data(data)
        time.sleep(read_interval_seconds)


if __name__ == "__main__":
    main()
