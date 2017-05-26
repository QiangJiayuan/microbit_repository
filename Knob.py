from microbit import *
while True:
    reading = pin0.read_analog() / 204
    if reading > 4.0:
        pos = 4
    elif reading > 3.0:
        pos = 3
    elif reading > 2.0:
        pos = 2
    elif reading > 1.0:
        pos = 1
    else:
        pos = 0
    column = ['0' for i in range(5)]
    column[pos] = '9'
    img = ((''.join(column)+':')*5)[0:-1]
    img = Image(img)
    display.show(img)
    sleep(200)
