import time
import serial
ser = serial.Serial('COM7', 115200)  # open serial port

command = b'Subir led\n\r'
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

    time.sleep(0.01)

print(reply)

ser.close()