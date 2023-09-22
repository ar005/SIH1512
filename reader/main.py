#for reading and writing the data from ldr and saving to csv

import serial
import csv
import time


#port and rate
ser = serial.Serial('/dev/ttyUSB0', 9600)  

csv_filename = "ldr1_data.csv"

# csv opening
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'SensorValue'])

try:
    while True:
        
        sensor_value = ser.readline().strip().decode('utf-8')  #get value from serial

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

       
       # print(f"Timestamp: {timestamp}, Sensor Value: {sensor_value}")

        #write
        with open(csv_filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, sensor_value])

except KeyboardInterrupt:
    pass

ser.close()

