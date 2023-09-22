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
        
        sensor_value = int(ser.readline().strip().decode('utf-8'))  #get value from serial

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        # calculate the light value 
        if sensor_value > 980:
            light_value = 0
        else:
            light_value = 980 - sensor_value

       
       # print(f"Timestamp: {timestamp}, Sensor Value: {sensor_value}")

        #write
        with open(csv_filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, sensor_value, light_value])

except KeyboardInterrupt:
    pass

ser.close()

