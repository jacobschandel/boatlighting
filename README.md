# Boat Lighting

## WARNING: Project NOT Complete or Bench Tested!!

This project controls a lighting system designed for a boat (in this case, a pontoon).

## Hardware

The following hardware was used for this project:

* Raspberry Pi Zero W
* Relay Board
* NPN Transistors
* IP67 LED Strip Lighting
* Push button

For more on the hardware for this project, please [see its page on Hackster.io](https://www.hackster.io).

## What These Do

The program consists of two files: `main.py` and `LightClass.py.`  The file `main.py` is the primary script that must run to execute this project.  The file `main.py` requires the `LightClass.py` file to function.  We use this because the strips used in this particular project are not wired directly into the Pi, but through relays.  Relays, unlike RGB LEDs, can not be used to merely dim the lights in this project, but may only be straight on or off.  This is done to prevent any urges to try using a relay at half power, which could have unintended consequences in the real world.

`main.py` takes a trio of relays, aided by `LightClass.py`, to allow a user to select a desired light color or color sequence using a push button to select the color sequence as well as an RGB LED to illustrate what color the user is picking (because the user may not be able to pick a color by looking over the side of a boat depending on where the control system is on the boat).  The following 11 configurations exist.

* **Blue**
* **Green**
* **Teal**
* **Red**
* **Magenta**
* **Amber**
* **White**
* **Ice:** a pattern of green, teal, and blue which resembles the colors of ice or an ocean
* **Fire:** a pattern of red, amber, and magenta which resemble a fire
* **American flag:** red, white, and blue to give a burst of American patriotism
* **Wild:** a cool pattern of colors which will surely make a boat stand out on the water (in a good way, of course)

As aforementioned, `LightClass.py` works with three relays, connected to the red, green, and blue elements of a (in this case) 12 V RGB LED strip.  These relays dictate which of the above configurations display on the LED strip.

## How to Use

This project was simply connected to a boat's existing lighting electrical system.  When the Pi boots, it is configured to execute this script.