import requests


class MasterService:

    def __init__(self, host, port, log_level):
        self.master_host = host
        self.master_port = port
        self.master_url = f'http://{self.master_host}:{self.master_port}/ingest/weather'
        self.log_level = log_level

    def record_data(self, data):

        if self.log_level == 'verbose':
            print(f"sending data: {data}")

        try:
            requests.post(self.master_url, json=data)
        except:
            pass
