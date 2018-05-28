"""
Jacob H. Schandel
boatlighting | LightClass.py
"""

from gpiozero import DigitalOutputDevice

class ExternalLighting:
    red = DigitalOutputDevice(17)
    green = DigitalOutputDevice(27)
    blue = DigitalOutputDevice(22)

    def off(self):
        red.off()
        green.off()
        blue.off()

    def blue(self):
        red.off()
        green.off()
        blue.on()

    def green(self):
        red.off()
        green.on()
        blue.off()

    def teal(self):
        red.off()
        green.on()
        blue.on()

    def red(self):
        red.on()
        green.off()
        blue.off()

    def purple(self):
        red.on()
        green.off()
        blue.on()

    def amber(self):
        red.on()
        green.on()
        blue.off()

    def white(self):
        red.on()
        green.on()
        blue.on()
