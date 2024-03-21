from sense_hat import SenseHat
import time
from weather import WeatherService
from client import ClientService
import os

read_interval_seconds = 60
sense = SenseHat()

green = (0, 255, 0)
white = (255, 255, 255)


def main():

    server_host = os.getenv('WEATHER_SERVER_HOST')
    server_port = os.getenv('WEATHER_SERVER_PORT')
    location = os.getenv('WEATHER_LOCATION')
    floor = os.getenv('WEATHER_FLOOR')
    cardinal_direction = os.getenv('CARDINAL_DIRECTION')
    log_level = os.getenv('WEATHER_LOG_LEVEL')

    if log_level is None or log_level == '':
        log_level = 'verbose'

    if server_host is None or server_host == '':
        print('no WEATHER_SERVER_HOST value')
        exit(1)
    elif server_port is None or server_port == '':
        print('no WEATHER_SERVER_PORT value')
        exit(2)
    elif location is None or location == '':
        print('no WEATHER_LOCATION value')
        exit(3)
    elif floor is None or floor == '':
        print('no WEATHER_FLOOR value')
        exit(4)
    elif cardinal_direction is None or cardinal_direction == '':
        print('no CARDINAL_DIRECTION value')
        exit(3)

    weather_svc = WeatherService(sense, location, cardinal_direction, floor)
    server_svc = ClientService(server_host, server_port, log_level)
    print('starting weather node')

    while True:
        data = weather_svc.get_data()
        server_svc.record_data(data)
        time.sleep(read_interval_seconds)


if __name__ == "__main__":
    main()
