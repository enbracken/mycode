#!/usr/bin/env python3
import time
import os
from gpiozero import LED, Button


def init_button_file():
    with open('button', 'w+') as f:
       button_state = f.write('unpressed')

def loop():
    led = LED(17)       # GPIO17, board pin 11
    button = Button(26) # GPIO26, board pin 37
    button.when_pressed = led.on
    button.when_released = led.off

    while True:
        with open('button', 'r') as f:
           button_state = f.read().strip()
           if button_state == 'unpressed':
              button.pin.drive_high()
           if button_state == 'pressed':
              button.pin.drive_low()

        if led.value == 0:
           led_emoji = "⚫"
        if led.value == 1:
           led_emoji = "🟡"
        print(f"{led_emoji} btn:{button.value}, led:{led.value}")

        time.sleep(1)

if __name__ == '__main__':
    print ('Program is starting ... \n')
    try:
        init_button_file()
        loop()
    except KeyboardInterrupt:
        os.remove('button')
        print ('\nProgram is exiting ...')

