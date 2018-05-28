"""
Jacob H. Schandel
boatlighting | main.py
"""

from gpiozero import DigitalOutputDevice
from gpiozero import RGBLED
from gpiozero import Button
from time import sleep

# light  controls
selectionLED = RGBLED(2,3,4)

red = DigitalOutputDevice(17)
green = DigitalOutputDevice(27)
blue = DigitalOutputDevice(22)
#TODO: more light relays to control in future?

# control buttons
#TODO: possible support for multiple light racks in future?
apply = Button(21)

print("PROGRAM ACTIVE")

#TODO: add a second buton, a while loop, and an ability to
#      perform a proper shutdown

selectionLED.color = (0,0,0)
while 1==1: #TODO: add in support for lightRelays1
    selectionLED.pulse(1,1,(0,0,1)) #blue
    red.off()
    green.off()
    blue.on()
    apply.wait_for_press()
    selectionLED.off()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(0,1,0)) #green
    red.off()
    green.on()
    blue.off()
    apply.wait_for_press()
    selectionLED.off()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(0,1,1)) #teal
    red.off()
    green.on()
    blue.on()
    apply.wait_for_press()
    selectionLED.off()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,0,0)) #red
    red.on()
    green.off()
    blue.off()
    apply.wait_for_press()
    selectionLED.off()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,0,1)) #magenta
    red.on()
    green.off()
    blue.on()
    apply.wait_for_press()
    selectionLED.off()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,1,0)) #yellowish-orange
    red.on()
    green.on()
    blue.off()
    apply.wait_for_press()
    selectionLED.off()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,1,1)) #white
    red.on()
    green.on()
    blue.on()
    apply.wait_for_press()
    selectionLED.off()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(0,0,1), (0,1,0)) #ice
    while apply.is_pressed == False:
        red.off()
        green.off()
        blue.on()
        sleep(1)
        red.off()
        green.on()
        blue.on()
        sleep(1)
        red.off()
        green.on()
        blue.off()
        sleep(1)
    selectionLED.off()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,0,0),(1,1,0)) #fire
    while apply.is_pressed == False:
        red.on()
        green.off()
        blue.off()
        sleep(1)
        red.on()
        green.on()
        blue.off()
        sleep(1)
        red.on()
        green.off()
        blue.on()
        sleep(1)
    selectionLED.off()
    apply.wait_for_release()

    selectionLED.pulse(1.25,1.25,(1,0,0),(0,0,1))#American flag
    while apply.is_pressed == False:
        red.on()
        green.off()
        blue.off()
        sleep(1)
        red.on()
        green.on()
        blue.on()
        sleep(1)
        red.off()
        green.off()
        sleep(1)
    selectionLED.off()
    apply.wait_for_release()

    selectionLED.pulse(.25,.25,(1,0,1), (0,1,1)) #WILD!!!
    while apply.is_pressed == False:
        red.on() #purple
        green.off()
        blue.on()
        sleep(0.5)
        red.on() #red
        green.off()
        blue.off()
        sleep(0.5)
        red.on()
        green.on() #amber
        blue.off()
        sleep(0.5)
        red.off() #green
        green.on()
        blue.off()
        sleep(0.5)
        red.off() #teal
        green.on()
        blue.on()
        sleep(0.5)
        red.off() #blue
        green.off()
        blue.on()
        sleep(0.5)
    selectionLED.off()
    apply.wait_for_release()
