#!/bin/bash
# გაშვება მთავარი სკრიპტისა
python -m venv env
env\Scripts\activate
pip install requirements.txt
python3 main.py