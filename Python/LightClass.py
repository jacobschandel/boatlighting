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
