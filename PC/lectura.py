import serial
import pandas as pd
import time
ser = serial.Serial('COM7',9600)
from datetime import datetime

df = pd.DataFrame(columns=['Temp','Light','Sound','Time','Date'])
start = time.perf_counter()
while len(df)<10:
    end = time.perf_counter()
    
    data = str(ser.readline())
    data = data[3:len(data)-6].split(",")
    now = datetime.now()
    fecha = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
    if len(str(now.day))<2:
        fecha = "0"+str(now.day)+"/"+str(now.month)+"/"+str(now.year)
    if len(str(now.month))<2:
        fecha = str(now.day)+"/0"+str(now.month)+"/"+str(now.year)
    if len(str(now.day))<2 and len(str(now.month))<2:
        fecha = "0"+str(now.day)+"/0"+str(now.month)+"/"+str(now.year)[2:4]
    hora = str(now.hour)+":"+str(now.minute)
    if (end - start) > 5:
        df = df.append({'Temp':float(data[1]),'Light':int(data[0]),'Sound':float(data[2]),'Time':hora,'Date':fecha},ignore_index=True)
        start = time.perf_counter()

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df)