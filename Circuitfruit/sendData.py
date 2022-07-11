# Escribe tu código aquí :-)
import time
import supervisor
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3
data = []

def scale_range(value):
    """Scale a value from 0-320 (light range) to 0-9 (NeoPixel range).
    Allows remapping light value to pixel position."""
    return round(value / 320 * 9)

data.append(cp.light)
data.append(cp.temperature)
data.append(cp.sound_level)
data.append(0)
data.append(0)
while True:
    cp.pixels[0] = (255, 255, 255)
    cp.pixels[1] = (255,255,255)
    
    peak = scale_range(cp.light)
    data[0] = cp.light
    data[1] = cp.temperature
    data[2] = cp.sound_level
    print(data)
    cp.pixels.show()
