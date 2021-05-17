# Original Python Script

While this file works, I am rewriting in C++ to add more features.

## What The File Does

The program consists of one file: `main.py`.  The file `main.py` is the primary script that must run to execute this project.  The strips used in this particular project are not wired directly into the Pi, but through relays.  Relays, unlike RGB LEDs, can not be used to merely dim the lights in this project, but may only be straight on or off.  So, rather than using the RGBLED class from gpiozero to run the strip lights, we use each element of the light (red, blue, green) as its own relay.  This is done to prevent any urges to try using a relay at half power, which could have unintended consequences in the real world.

`main.py` takes a trio of relays and a control system ran by a Raspberry Pi to allow a user to select a desired light color or color sequence using a push button to select the color sequence as well as an RGB LED to illustrate what color the user is picking (because the user may not be able to pick a color by looking over the side of a boat depending on where the control system is on the boat).  The following 11 configurations exist.

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

## How to Use

This project was simply connected to a boat's existing lighting electrical system.  When the Pi boots, it is configured to execute this script by adding the following line to the /etc/rc.local file on the Pi right before the line that reads `exit 0`, assuming you clone this repository to your Pi's desktop:

```bash
python3 /home/pi/Desktop/boatlighting/Python/main.py
```

If you do not know how to edit /etc/rc.local, run the following command:

```bash
sudo leafpad /etc/rc.local
```

This will give you an easy-to-use GUI text editor to finish this part of setup.

For hardware setup and to see how to run this physically, please [see its page on Hackster.io](https://www.hackster.io).
