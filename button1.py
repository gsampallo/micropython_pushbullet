from machine import Pin
import time

button = Pin(4,Pin.IN,Pin.PULL_UP)

start = time.ticks_ms()

while True:
    if(button.value() == 0):
        delta = time.ticks_diff(time.ticks_ms(), start)
        if(delta > 100):
            print ("Boton presionado")
            start = time.ticks_ms()
