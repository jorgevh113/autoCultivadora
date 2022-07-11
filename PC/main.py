import time
import serial
import pandas as pd
from datetime import datetime
import numpy as np


ser = serial.Serial('COM7', 115200)  # open serial port

command = b'[3 0.1 0]\n\r'
ser.write(command)     # write a string

omitir = ser.readline()

reply = ser.readline()
df = pd.DataFrame(columns=['Temp','Light','Sound','Time','Date'])
serData = str(reply)[3:len(reply)-6].split(",")
now = datetime.now()
fecha = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
if len(str(now.day))<2:
    fecha = "0"+str(now.day)+"/"+str(now.month)+"/"+str(now.year)
if len(str(now.month))<2:
    fecha = str(now.day)+"/0"+str(now.month)+"/"+str(now.year)
if len(str(now.day))<2 and len(str(now.month))<2:
    fecha = "0"+str(now.day)+"/0"+str(now.month)+"/"+str(now.year)[2:4]
hora = str(now.hour)+":"+str(now.minute)
hd = [hora,fecha]
data = serData+hd
df = df.append({'Temp':float(data[1]),'Light':int(data[0]),'Sound':float(data[2]),'Time':hora,'Date':fecha},ignore_index=True)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df)

ser.close()