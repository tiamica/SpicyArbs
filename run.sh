#!/bin/bash

echo "=== Install requirements ==="
pip install -r requirements.txt

echo "=== Build the results ==="
python main_webscraper.py

echo "=== Publish as index.html ==="
cp results.html index.html


