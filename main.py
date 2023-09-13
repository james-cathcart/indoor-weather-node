from sense_emu import SenseHat
import time
from weather import WeatherService
from master import MasterService
import os


read_interval_seconds = 2
sense = SenseHat()

green = (0, 255, 0)
white = (255, 255, 255)

master_host = os.getenv('MASTER_HOST')
master_port = os.getenv('MASTER_PORT')

def main():
   
   weather_svc = WeatherService(sense, "office")
   master_svc = MasterService(master_host, master_port)
   print('starting weather node')

   while True:
       data = weather_svc.get_data()
       master_svc.record_data(data)
       time.sleep(read_interval_seconds)


if __name__ == "__main__":
    main()
