import time
import serial
ser = serial.Serial('COM7', 115200)  # open serial port

command = b'[3 0.1 0]\n\r'
ser.write(command)     # write a string

reply = ser.readline()
print(reply)

ser.close()