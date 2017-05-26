from microbit import *

while True:
    reading1 = accelerometer.get_x()
    if reading1 > 20:
        display.show("L")
    elif reading1 < -20:
        display.show("R")
    else:
        display.show("-")
