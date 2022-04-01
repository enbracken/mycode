import serial
import sparklines
import sys
from time import sleep
from termcolor import colored

ser = serial.Serial("serial", 9600)  # Open port with baud rate
output_ctr = 0
while True:
    raw_data = ser.read()  # read serial port
    data_left = ser.inWaiting()  # check for remaining byte
    raw_data += ser.read(data_left)
    # read one byte at a time from raw_data
    for sensor_reading in raw_data:
        output_ctr += 1
        spark = sparklines.sparklines([sensor_reading], minimum=0, maximum=255)[0]
        if sensor_reading < 50:
            color_spark = colored(spark, "red")
        if 110 > sensor_reading > 50:
            color_spark = colored(spark, "yellow")
        if 155 > sensor_reading > 110:
            color_spark = colored(spark, "green")
        if 175 > sensor_reading > 155:
            color_spark = colored(spark, "yellow")
        if 175 < sensor_reading:
            color_spark = colored(spark, "red")
        if (output_ctr % 64) == 0:
            sys.stdout.write("\b" * 64)
        print(color_spark, end="")
        sys.stdout.flush()

