# Indoor Weather Node

This repository supports the Raspberry Pi SenseHat Indoor Weather application

## Overview
This is the Weather Node portion of the Indoor Weather application. This uses a Raspberry Pi and a SenseHAT to read weather data and then send it to the Weather Server for further processing/persistence.

# Setup
## Configuration
You must have three environment variables set:
- **_MASTER_HOST_** - Weather Server host 
- **_MASTER_PORT_** - Weather Server port
- **_WEATHER_LOCATION_** - Weather Node location (i.e. office, kitchen, etc...)

## Installation
Install SenseHat
```
sudo apt install sense-hat
```
Clone repository to device
```
git clone https://github.com/james-cathcart/indoor-weather-node.git
```
Run application
```
python3 main.py
```

## Run as Service
tbd

# Development
## Architecture
![](docs/classes.png)

## Deployment
![](docs/deployment.png)