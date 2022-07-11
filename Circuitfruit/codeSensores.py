# Escribe tu código aquí :-)
import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

def scale_range(value):
    """Scale a value from 0-320 (light range) to 0-9 (NeoPixel range).
    Allows remapping light value to pixel position."""
    return round(value / 320 * 9)

while True:
    peak = scale_range(cp.light)
    print("Luminosidad: "+str(cp.light))
    print("Temperatura: "+str(cp.temperature))
    print(int(peak))

    for i in range(10):
        if i <= peak:
            cp.pixels[i] = (0, 255, 255)
        else:
            cp.pixels[i] = (0, 0, 0)
    cp.pixels.show()
    time.sleep(0.05)