#!/usr/bin/env python3
import random
import time
import os

read_value = random.randint(0, 1024)  # simulated read from higher fidelity data source
while True:
    read_value = read_value + random.randint(-256, 256)
    if read_value > 1023:
        read_value = 1023
    if read_value < 0:
        read_value = 0
    serial_value = int(
        read_value / 4
    )  # compress data in same way as the arduino sketch
    raw_value = serial_value.to_bytes(1, "big")
    os.write(1, raw_value)
    time.sleep(0.1)

