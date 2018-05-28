"""
Jacob H. Schandel
boatlighting | main.py
"""

from gpiozero import RGBLED
from gpiozero import Button
from LightClass import Lighting
from time import sleep

# light  controls
selectionLED = RGBLED(2,3,4)

redUnderBoat = 17
greenUnderBoat = 27
blueUnderBoat = 22
lightRelays1 = Lighting(r=int(redUnderBoat), g=int(greenUnderBoat), b=int(blueUnderBoat))
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
    lightRelays1.blue()
    apply.wait_for_press()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(0,1,0)) #green
    lightRelays1.green()
    apply.wait_for_press()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(0,1,1)) #teal
    lightRelays1.teal()
    apply.wait_for_press()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,0,0)) #red
    lightRelays1.red()
    apply.wait_for_press()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,0,1)) #magenta
    lightRelays1.purple()
    apply.wait_for_press()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,1,0)) #yellowish-orange
    lightRelays1.amber()
    apply.wait_for_press()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,1,1)) #white
    lightRelays1.white()
    apply.wait_for_press()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(0,0,1), (0,1,0)) #ice
    while apply.is_pressed == False:
        lightRelays1.blue()
        sleep(1)
        lightRelays1.teal()
        sleep(1)
        lightRelays1.green()
        sleep(1)
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,0,0),(1,1,0)) #fire
    while apply.is_pressed == False:
        lightRelays1.red()
        sleep(1)
        lightRelays1.amber()
        sleep(1)
        lightRelays1.purple()
        sleep(1)
    apply.wait_for_release()

    selectionLED.pulse(1.25,1.25,(1,0,0),(0,0,1))#American flag
    while apply.is_pressed == False:
        lightRelays1.red()
        sleep(1)
        lightRelays1.white()
        sleep(1)
        lightRelays1.blue()
        sleep(1)
    apply.wait_for_release()

    selectionLED.pulse(.25,.25,(1,0,1), (0,1,1)) #WILD!!!
    while apply.is_pressed == False:
        lightRelays1.magenta()
        sleep(0.5)
        lightRelays1.red()
        sleep(0.5)
        lightRelays1.amber()
        sleep(0.5)
        lightRelays1.green()
        sleep(0.5)
        lightRelays1.teal()
        sleep(0.5)
        lightRelays1.blue()
        sleep(0.5)
    apply.wait_for_release()
