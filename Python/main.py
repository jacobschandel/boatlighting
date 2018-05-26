"""
Jacob H. Schandel
boatlighting | main.py
"""

from gpiozero import RGBLED
from gpiozero import Button

# ints to used
choice = 0 # option selected, default is ALL LEDS OFF  TODO:change to 0
max = 11

# light  controls
selectionLED = RGBLED(2,3,4)
lightRelays1 = RGBLED(17,27,22) #TODO: make this a class
#TODO: more light relays to control in future?

# control buttons
#TODO: possible support for multiple light racks in future?
apply = Button(21)

print("PROGRAM ACTIVE")

selectionLED.color = (0,0,0)
while 1==1: #TODO: add in support for lightRelays1
    selectionLED.off() #LEDs off, Pi on unless powered off
    apply.wait_for_press()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(0,0,1)) #blue
    apply.wait_for_press()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(0,1,0)) #green
    apply.wait_for_press()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(0,1,1)) #teal
    apply.wait_for_press()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,0,0)) #red
    apply.wait_for_press()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,0,1)) #magenta
    apply.wait_for_press()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,1,0)) #yellowish-orange
    apply.wait_for_press()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,1,1)) #white
    apply.wait_for_press()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(0,0,1), (0,1,0)) #ice
    apply.wait_for_press()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,0,0),(1,1,0)) #fire
    apply.wait_for_press()
    apply.wait_for_release()

    selectionLED.pulse(1.25,1.25,(1,0,0),(0,0,1))#American flag
    apply.wait_for_press()
    apply.wait_for_release()

    selectionLED.pulse(.25,.25,(1,0,1), (0,1,1)) #WILD!!!
    apply.wait_for_press()
    apply.wait_for_release()
