import firebase_admin
from firebase_admin import db, credentials
import RPi.GPIO as GPIO
import time

cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred,{
        'databaseURL': 'https://greenhouse-af8a7-default-rtdb.firebaseio.com/'
    })

MOISTURE_PIN= 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOISTURE_PIN, GPIO.IN)


def read_moisture():
    return GPIO.input(MOISTURE_PIN)

while True:
    moisture_level = read_moisture()
    ref = db.reference("moisture_data")
    ref.push({"moisture": moisture_level, "timestamp": time.time()})
    print(f"Sent moisture data: {moisture_level}")
    time.sleep(3600)