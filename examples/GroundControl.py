from microbit import *
import radio
radio.on()

'''
To use:
Download this code to a micro:bit and keep it plugged in to a computer.
Click 'Show serial' on the bottom left of the editor.
Watch the messages come through from the satellites!
'''

display.show(Image.DUCK)

while True:
    message = radio.receive()
    if message:
        print()
        print(message)
        sleep(200)