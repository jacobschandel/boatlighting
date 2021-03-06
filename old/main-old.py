"""
Jacob H. Schandel
boatlighting | main-old.py

This program is the original version of the boat light program I wrote.
It works fine, but I wanted to make the code cleaner by using multiple 
compilation so my next addition to the program is easier.
"""

from gpiozero import DigitalOutputDevice
from gpiozero import RGBLED
from gpiozero import Button
from time import sleep
import subprocess

# light  controls
selectionLED = RGBLED(2,3,4)

red = DigitalOutputDevice(17)
green = DigitalOutputDevice(27)
blue = DigitalOutputDevice(22)
#TODO: more light relays to control in future?

# control buttons
#TODO: possible support for multiple light racks in future?
apply = Button(21)
kill = Button(20)

print("PROGRAM ACTIVE")

red.off()
green.off()
blue.off()

selectionLED.color = (0,0,0)

while kill.is_pressed == False: #TODO: add in support for lightRelays1
    selectionLED.pulse(1,1,(0,0,1)) #blue
    blue.on()
    apply.wait_for_press()
    selectionLED.off()
    blue.off()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(0,1,0)) #green
    green.on()
    apply.wait_for_press()
    selectionLED.off()
    green.off()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(0,1,1)) #teal
    green.on()
    blue.on()
    apply.wait_for_press()
    selectionLED.off()
    green.off()
    blue.off()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,0,0)) #red
    red.on()
    apply.wait_for_press()
    selectionLED.off()
    red.off()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,0,1)) #magenta
    red.on()
    blue.on()
    apply.wait_for_press()
    selectionLED.off()
    red.off()
    blue.off()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,1,0)) #yellowish-orange
    red.on()
    green.on()
    apply.wait_for_press()
    selectionLED.off()
    red.off()
    green.off()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,1,1)) #white
    red.on()
    green.on()
    blue.on()
    apply.wait_for_press()
    selectionLED.off()
    red.off()
    blue.off()
    green.off()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(0,0,1), (0,1,0)) #ice
    while apply.is_pressed == False:
        green.off()
        blue.on()
        sleep(1)
        green.on()
        sleep(1)
        blue.off()
        sleep(1)
    selectionLED.off()
    green.off()
    apply.wait_for_release()

    selectionLED.pulse(1,1,(1,0,0),(1,1,0)) #fire
    while apply.is_pressed == False:
        red.on()
        blue.off()
        sleep(1)
        green.on()
        sleep(1)
        green.off()
        blue.on()
        sleep(1)
    selectionLED.off()
    red.off()
    blue.off()
    apply.wait_for_release()

    selectionLED.pulse(1.25,1.25,(1,0,0),(0,0,1))#American flag
    while apply.is_pressed == False:
        red.on()
        blue.off()
        sleep(1)
        green.on()
        blue.on()
        sleep(1)
        red.off()
        green.off()
        sleep(1)
    selectionLED.off()
    blue.off()
    apply.wait_for_release()

    selectionLED.pulse(.25,.25,(1,0,1), (0,1,1)) #WILD!!!
    while apply.is_pressed == False:
        red.on() #purple
        blue.on()
        sleep(0.5)
        blue.off() #red
        sleep(0.5)
        green.on() #amber
        sleep(0.5)
        red.off() #green
        sleep(0.5)
        blue.on() #teal
        sleep(0.5)
        green.off() #blue
        sleep(0.5)
    selectionLED.off()
    blue.off()
    apply.wait_for_release()
    
red.off()
green.off()
blue.off()

selectionLED.color = (1,1,1)

command = "/usr/bin/sudo /sbin/shutdown now"
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]
print(output)
