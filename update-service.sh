#!/bin/bash

echo "stopping service..."
sudo systemctl stop weather-node
echo "updating application..."
git pull
echo "starting service..."
sudo systemctl start weather-node
echo "update complete"
