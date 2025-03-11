import firebase_admin
from firebase_admin import credentials, firestore  # Import firestore
import time
from grove.adc import ADC
from seeed_dht import DHT

cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred) 

db = firestore.client()  sensor = DHT("11", 0)
adc = ADC()

while True:
    soil_moisture = adc.read(0)
    timestamp = time.time()

    doc_ref = db.collection('moisture_data').document()
    doc_ref.set({
        'moisture': soil_moisture,
        'timestamp': timestamp
    })

    print(f"Sent moisture data: {soil_moisture}")
    time.sleep(10)

