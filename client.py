import requests


class ClientService:

    def __init__(self, host, port, log_level):
        self.server_host = host
        self.server_port = port
        self.server_url = f'http://{self.server_host}:{self.server_port}/ingest/weather'
        self.log_level = log_level

    def record_data(self, data):

        print(f"sending data: {data}")

        res = None
        try:
            res = requests.post(self.server_url, json=data)
        except:
            pass

        if res is not None:
            print(res)

