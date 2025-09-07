# Imports go at the top
from microbit import *
import radio
radio.on()

radio.send('PyConUK connected')

# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image.HAPPY)
    sleep(1000)

    light = display.read_light_level()
    print(light)

    if light < 80:
        radio.send('PyConUK low power')

    acc = accelerometer.get_strength()
    print(acc)

    if acc > 1200 or acc < 800:
        radio.send('PyConUK unstable')
