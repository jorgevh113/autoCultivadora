import time
import board
from digitalio import DigitalInOut, Direction, Pull
import digitalio

# LED setup.
rel = DigitalInOut(board.D2) #A5
# For QT Py M0. QT Py M0 does not have a D13 LED, so you can connect an external LED instead.
# led = DigitalInOut(board.SCK)
rel.direction = Direction.OUTPUT
buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.DOWN

while True:
    if buttonA.value:
        rel.value = True
    else:
        rel.value = False