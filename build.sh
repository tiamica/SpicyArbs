#!/bin/bash

echo "=== Install Python 3.7 ==="

sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.7

echo "=== Install requirements ==="
pip install -r requirements.txt

echo "=== Build the results ==="
python main_webscraper.py

echo "=== Publish as index.html ==="
cp results.html index.html


