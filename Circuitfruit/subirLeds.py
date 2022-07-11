import supervisor
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

light = 0
while True:
    if supervisor.runtime.serial_bytes_available:
        value = input().strip()
        comando = str(value)
        if comando == 'Subir led':
            print("Subiendo leds")
            light += 1
            for i in range(light):
                cp.pixels[i] = (255, 255, 255)
                cp.pixels.show()