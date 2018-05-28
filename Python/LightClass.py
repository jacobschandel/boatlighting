"""
Jacob H. Schandel
boatlighting | LightClass.py
"""

from gpiozero import DigitalOutputDevice

class ExternalLighting:
    def __init__ (x = False):
        self.red = DigitalOutputDevice(17)
        self.green = DigitalOutputDevice(27)
        self.blue = DigitalOutputDevice(22)

    def off():
        self.red.off()
        self.green.off()
        self.blue.off()

    def blue():
        self.red.off()
        self.green.off()
        self.blue.on()

    def green():
        self.red.off()
        self.green.on()
        self.blue.off()

    def teal():
        self.red.off()
        self.green.on()
        self.blue.on()

    def red():
        self.red.on()
        self.green.off()
        self.blue.off()

    def purple():
        self.red.on()
        self.green.off()
        self.blue.on()

    def amber():
        self.red.on()
        self.green.on()
        self.blue.off()

    def white():
        self.red.on()
        self.green.on()
        self.blue.on()
