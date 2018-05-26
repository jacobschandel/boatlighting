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
colorPick = Button(16)
#TODO: possible support for multiple light racks in future?
apply = Button(21)

print("PROGRAM ACTIVE")

selectionLED.color = (0,0,0)
while 1==1:
    isChanged = 0
    if colorPick.is_pressed:
        choice = choice + 1
        if choice == max:
            choice = 0
            isChanged = 1
    if isChanged == 1:
        #light choices
        if choice == 0: #off (lights go dark, Pi still on!)
            selectionLED.off
        elif choice == 1: #blue
            selectionLED.pulse(1,1,(0,0,1))
        elif choice == 2: #green
            selectionLED.pulse(1,1,(0,1,0))
        elif choice == 3: #teal
            selectionLED.pulse(1,1,(0,1,1))
        elif choice == 4: #red
            selectionLED.pulse(1,1,(1,0,0))
        elif choice == 5: #purple
            selectionLED.pulse(1,1,(1,0,1))
        elif choice == 6: #yellowish-orange
            selectionLED.pulse(1,1,(1,1,0))
        elif choice == 7: #white
            selectionLED.pulse(1,1,(1,1,1))
        elif choice == 8: #ice
            selectionLED.pulse(1,1,(0,0,1), (0,1,0))
        elif choice == 9: #fire
            selectionLED.pulse(1,1,(1,0,0),(1,1,0))
        else: #wild
            selectionLED.pulse(.25,.25,(1,0,1), (0,1,1))

"""if apply.is_pressed:
    lightRelays1.set(choice)"""
