import firebase_admin
from firebase_admin import db, credentials
import time
from grove.adc import ADC
from seeed_dht import DHT

cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred,{
        'databaseURL': 'https://greenhouse-af8a7-default-rtdb.firebaseio.com/'
    })

sensor = DHT("11",0)
adc = ADC()

while True:
    soil_moisture = adc.read(0)
    ref = db.reference("moisture_data")
    ref.set({
            'moisture': soil_moisture,
            'timestamp': time.time()
        })
    ref.push({"moisture": soil_moisture, "timestamp": time.time()})
    print(f"Sent moisture data: {soil_moisture}")
    time.sleep(10)