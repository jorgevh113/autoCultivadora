import time
import serial
ser = serial.Serial('COM7', 115200)  # open serial port

command = b'[5 0.1 200]\n\r'
ser.write(command)     # write a string

reply = b''

for i in command:
    a = ser.read() # Read the loopback chars and ignore

while True:
    a = ser.read()
    if a== b'\r':
        break
    else:
        reply += a

print(reply)

ser.close()