#UTILIZANDO LIBRERIA REQUESTS

import Adafruit_DHT
import time
import requests

sensor = Adafruit_DHT.DHTXX
pin = pin_GPIO
url = "https://api.thingspeak.com/update?api_key=APIKEY"

while True: 
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
    
    if humedad is not None and temperatura is not None:
        print(f'Temperatura={temperatura:.2f}*C  Humedad={humedad:.2f}%')
    else:
        print('Fallo la lectura del sensor.Intentar de nuevo')

    f=requests.get(url+"&field1="+str(temperatura)+"&field2="+str(humedad))
    
    time.sleep(5) 
