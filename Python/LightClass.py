"""
Jacob H. Schandel
boatlighting | LightClass.py
"""

from gpiozero import DigitalOutputDevice

class Lighting:
    def __init__ (r, g, b):
        self.red = DigitalOutputDevice(r)
        self.green = DigitalOutputDevice(g)
        self.blue = DigitalOutputDevice(b)

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
