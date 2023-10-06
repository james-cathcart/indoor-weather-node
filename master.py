import requests

class MasterService:

    def __init__(self, host, port):
        self.master_host = host
        self.master_port = port
        self.master_url = f'http://{self.master_host}:{self.master_port}/ingest/weather'

    def record_data(self, data):
        try:
            res = requests.post(self.master_url, json=data)
        except:
            print('call to master server failed', res.text)
