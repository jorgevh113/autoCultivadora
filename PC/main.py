############## LIBRERÍAS ##################
import time
from xml.etree.ElementTree import tostring
import serial
import pandas as pd
from datetime import datetime
import numpy as np

############# VARIABLES GLOBALES ##########

ser = serial.Serial('COM7', 115200)  #Abrir puerto serial
df = pd.DataFrame(columns=['Temp','Light','Sound','Time','Date']) #Crear dataframe

############# FUNCIONES ###################
def obtenerFecha():
    now = datetime.now() #Se obtiene la fecha y hora actual
    fecha = str(now.day)+"/"+str(now.month)+"/"+str(now.year) #Se convierte a string la fecha

    ############ DAR FORMATO DD/MM/AA A LA FECHA###################
    if len(str(now.day)) < 2:
        fecha = "0"+str(now.day)+"/"+str(now.month)+"/"+str(now.year)
    if len(str(now.month)) < 2:
        fecha = str(now.day)+"/0"+str(now.month)+"/"+str(now.year)
    if len(str(now.day)) < 2 and len(str(now.month)) < 2:
        fecha = "0"+str(now.day)+"/0"+str(now.month)+"/"+str(now.year)[2:4]

    hora = str(now.hour)+":"+str(now.minute) #String de la hora
    ############ DAR FORMATO HH/MM A LA HORA ##################### 
    if len(str(now.hour)) < 2:
        hora = "0"+str(now.hour)+":"+str(now.minute)
    if len(str(now.min)) < 2:
        hora = str(now.hour)+":0"+str(now.minute)
    if len(str(now.hour)) < 2 and len(str(now.min)) < 2:
        hora = "0"+str(now.hour)+":0"+str(now.minute)
    hd = [hora,fecha] #Vector con hora y fecha
    return hd

#Esta debería ser la función para obtener los valores de los botones y actualizarlos
#def funcionBotones():


command = str([3,0.3,400])+'\n\r' #Así se hace un string para ser transmitido por puerto serial
ser.write(command.encode())     #Enviar matriz con valores de actuadores al puerto serial

omitir = ser.readline() #Se tiene que hacer porque luego se lee el mismo valor que fue enviado

############################## CICLO PARA  LECTURA Y ENVÍO DE DATOS #############################
while True:

    ################# SI HAY BYTES POR LEER EN EL PUERTO SERIAL ##################################
    if ser.in_waiting>0: #in_waiting indica cuántos bytes quedan por leer en el puerto serial
        reply = ser.readline() #Lectura del puerto serial
        serData = str(reply)[3:len(reply)-6].split(",") #Convertir datos a arreglo de strings
        hd = obtenerFecha() #Función para obtener fecha y hora en un arreglo
        data = serData+hd #Se crea arreglo de 5 elementos donde se guarda Temperatura, Luminosidad, Sonido, Hora y Fecha
        df = df.append({'Temp':float(data[1]),'Light':int(data[0]),'Sound':float(data[2]),'Time':hd[0],'Date':hd[1]},ignore_index=True) #imprimir dataframe
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
            print(df)

ser.close()