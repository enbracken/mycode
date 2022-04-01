#!/usr/bin/env python3
import time
from gpiozero import LED

def loop():
    ledPin = 17
    led = LED(ledPin)
    while True:
        led.on()
        print (f'led turned on  >>> {led.value}')
        time.sleep(1)
        led.off()
        print (f'led turned off <<< {led.value}')
        time.sleep(1)

if __name__ == '__main__':
    print ('Program is starting ... \n')
    try:
        loop()
    except KeyboardInterrupt:
        print ('\nProgram is exiting ...')

