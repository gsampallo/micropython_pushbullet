import network
from machine import Pin
import time
import json
import urequests
from wlan import do_connect

do_connect()

button = Pin(4,Pin.IN,Pin.PULL_UP)

start = time.ticks_ms()

apiKey = 'XXXXXXXXXXXXXXXXXXXXXXXX' #reemplazar por la propia API KEY

url = "https://api.pushbullet.com/v2/pushes"
headers = {'Access-Token': apiKey, 'Content-Type': 'application/json'}

data = {'type':'note','body':'Mensaje desde MicroPython','title':'MicroPython'}
dataJSON = json.dumps(data)




while True:
    if(button.value() == 0):
        delta = time.ticks_diff(time.ticks_ms(), start)
        if(delta > 5000):
            print("Enviando mensaje")
            r = urequests.post(url, headers=headers,data=dataJSON)
            print(r.json()['receiver_email'])
            start = time.ticks_ms()