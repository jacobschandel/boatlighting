"""
Jacob H. Schandel
boatlighting | LightClass.py
"""

from gpiozero import DigitalOutputDevice

class ExternalLighting:
    def __init__ (self):
        self.red = DigitalOutputDevice(17)
        self.green = DigitalOutputDevice(27)
        self.blue = DigitalOutputDevice(22)

    def off(self):
        self.red.off()
        self.green.off()
        self.blue.off()

    def blue(self):
        self.red.off()
        self.green.off()
        self.blue.on()

    def green(self):
        self.red.off()
        self.green.on()
        self.blue.off()

    def teal(self):
        self.red.off()
        self.green.on()
        self.blue.on()

    def red(self):
        self.red.on()
        self.green.off()
        self.blue.off()

    def purple(self):
        self.red.on()
        self.green.off()
        self.blue.on()

    def amber(self):
        self.red.on()
        self.green.on()
        self.blue.off()

    def white(self):
        self.red.on()
        self.green.on()
        self.blue.on()
