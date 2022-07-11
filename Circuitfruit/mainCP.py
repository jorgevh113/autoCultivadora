###################### LIBRERÍAS ################
import supervisor
import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False

data = [0,0,0]
param = [0,0,0]


################# FUNCIONES ####################

#Función para cambiar estado de los leds
def prenderLeds(cantLuces,brightness):
    cp.pixels.brightness = brightness #Cambiar brillo 
    
    #Ciclo para prender y apagar cierta cantidad de leds
    for i in range(cantLuces):
            cp.pixels[i] = (255, 255, 255)
    for i in range(cantLuces,len(cp.pixels)):
        cp.pixels[i] = (0,0,0)
    cp.pixels.show() #Actaulizar leds
    return

#Función para reproducir cierta frecuencia de sonido
def cambiarSonido(frecuencia):
    cp.start_tone(frecuencia)
    return



start = time.time() #Empezar contador


############# CICLO PARA LECTURA Y ENVÍO DE DATOS #############
while True:
    end = time.time() #Obtener cuánto tiempo ha transcurrido
    cambiarSonido(int(param[2])) #Empezar sonido
    
    ########## MONITOREAR SI HAY BYTES POR LEER EN PUERTO SERIAL #########
    if supervisor.runtime.serial_bytes_available:
        cp.stop_tone() #Se tiene que parar el sonido para ejecutar otras instrucciones
        param = str(input().strip()) #Obtener string de los datos recibidos
        param = param[1:len(param)-1].split(",") #hacer un arrego de string de los datos de puerto serial
        prenderLeds(int(param[0]),float(param[1])) #Función para prender cierta cantidad de leds con una luminosidad específica
    
    ######### REAIZAR ENVÍO DE DATOS DE SENSORES CADA CIERTO TIEMPO ########
    if (end-start > 5):
        cp.stop_tone() #Se tiene que parar el sonido para ejecutar otras instrucciones
        data[0] = cp.light #Obtener valor de sensor de luminosidad
        data[1] = cp.temperature #Obtener valor de sensor de temperatura
        data[2] = cp.sound_level #Obtener valor de sensor de ruido
        print(data) #Mandar matriz de datos al puerto serial
        start = time.time() #Reiniciar cronómetro




