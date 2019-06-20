// Jacob H. Schandel
// boatlighting
// main.cpp

// Purpose: this file in the program is responsible for driving the rest of the program.

#include <iostream>
#include <cstdlib>
#include <wiringPi.h>
#include "ws2812-rpi.h"

// Note: wiringPi.h is part of Raspbian, and may show as an error when writing code on a device
//       not Raspbian-based, such as a Windows PC code editor with debugging.

using namespace std;  // TODO: replace with proper usings.

// GPIO CONSTANTS
// ==============

// The following is the GPIO assignments for the project, defined as const ints:
//     Board Indicator RGB (optional): 2, 3, 4, for red, green, and blue, respectively
//     Red Relay for Exterior: 17
//     Green Relay for Exterior: 27
//     Blue Relay for Exterior: 22
//     Color Toggle: 21
//     Reset System Button: 20
//     Signal Pin for Interior: 18

const int RGB_LED[3] = {2, 3, 4};
const int RGB_EXT[3] = {17, 27, 22};
const int RGB_INT_ADDR = 18;  // this is defined in the WS2812-rpi library
const int TOGGLE = 21;
const int RESET = 20;

// ********************************************************************************************
// ********************************************************************************************
// ********************************************************************************************
// ********************************************************************************************

// PROTOTYPES
// ==========

void initializeStandardGPIO();

void blue(NeoPixel*);
void green(NeoPixel*);
void teal(NeoPixel*);
void red(NeoPixel*);
void magenta(NeoPixel*);
void amber(NeoPixel*);
void white(NeoPixel*);
void ice(NeoPixel*);
void fire(NeoPixel*);
void flagAmerican(NeoPixel*);
void wild(NeoPixel*);

bool shutdownScript();

void cellConnect();

// ********************************************************************************************
// ********************************************************************************************
// ********************************************************************************************
// ********************************************************************************************

// MAIN
// ====

int main ()
{
    initializeStandardGPIO();
    NeoPixel * n = new NeoPixel(25); // TODO: replace with proper LED count

    int selection = 0;
    while (true)
    {
        if (digitalRead(TOGGLE) == 1)
        {
            ++selection;
            if (selection >= 11)
                selection = 0;
        }
        else if (digitalRead(RESET) == 1)
        {
            bool fightOrFlight = shutdownScript();
            if (fightOrFlight)
            {
                system("shutdown now");
            }
        }
        switch (selection)
        {
            case 0:
                blue(n);
                break;
            case 1:
                green(n);
                break;
            case 2:
                teal(n);
                break;
            case 3:
                red(n);
                break;
            case 4:
                magenta(n);
                break;
            case 5:
                amber(n);
                break;
            case 6:
                white(n);
                break;
            case 7:
                ice(n);
                break;
            case 8:
                fire(n);
                break;
            case 9:
                flagAmerican(n);
                break;
            case 10:
                wild(n);
                break;
            default:
                // TODO: app partner
                break;
        }
    }
    // TODO: do stuff
    return 0;
}

// ********************************************************************************************
// ********************************************************************************************
// ********************************************************************************************
// ********************************************************************************************

// FUNCTION DEFINITIONS
// ====================

// initializes the pins for the necessary uses as inputs and outputs
// inputs: none
// outputs: sets pins to input and output as needed
void initializeStandardGPIO()
{
    wiringPiSetup();
    
    // inputs
    pinMode(RESET, INPUT);
    pinMode(TOGGLE, INPUT);

    // outputs
    pinMode(RGB_LED[0], OUTPUT);
    pinMode(RGB_LED[1], OUTPUT);
    pinMode(RGB_LED[2], OUTPUT);

    pinMode(RGB_EXT[0], OUTPUT);
    pinMode(RGB_EXT[1], OUTPUT);
    pinMode(RGB_EXT[2], OUTPUT);
}

// sets lights to the color solid blue
// inputs: 
// outputs: 
void blue(NeoPixel * n)
{
    // TODO: define function
    digitalWrite(RGB_EXT[0], 0);
    digitalWrite(RGB_EXT[1], 0);
    digitalWrite(RGB_EXT[2], 1);
}

//
// inputs: 
// outputs: 
void green(NeoPixel * n)
{
    // TODO: define function
    digitalWrite(RGB_EXT[0], 0);
    digitalWrite(RGB_EXT[1], 1);
    digitalWrite(RGB_EXT[2], 0);
}

//
// inputs: 
// outputs: 
void teal(NeoPixel * n)
{
    // TODO: define function
    digitalWrite(RGB_EXT[0], 0);
    digitalWrite(RGB_EXT[1], 1);
    digitalWrite(RGB_EXT[2], 1);
}

//
// inputs: 
// outputs: 
void red(NeoPixel * n)
{
    // TODO: define function
    digitalWrite(RGB_EXT[0], 1);
    digitalWrite(RGB_EXT[1], 0);
    digitalWrite(RGB_EXT[2], 0);
}

//
// inputs: 
// outputs: 
void magenta(NeoPixel * n)
{
    // TODO: define function
    digitalWrite(RGB_EXT[0], 1);
    digitalWrite(RGB_EXT[1], 0);
    digitalWrite(RGB_EXT[2], 1);
}

//
// inputs: 
// outputs: 
void amber(NeoPixel * n)
{
    // TODO: define function
    digitalWrite(RGB_EXT[0], 1);
    digitalWrite(RGB_EXT[1], 1);
    digitalWrite(RGB_EXT[2], 0);
}


//
// inputs: 
// outputs: 
void white(NeoPixel * n)
{
    // TODO: define function
    digitalWrite(RGB_EXT[0], 1);
    digitalWrite(RGB_EXT[1], 1);
    digitalWrite(RGB_EXT[2], 1);
}

//
// inputs: 
// outputs: 
void ice(NeoPixel * n)
{
    blue(n);
    usleep(1000000);
    teal(n);
    usleep(1000000);
    green(n);
    usleep(1000000);
    // TODO: define function for NeoPixels
}

//
// inputs: 
// outputs: 
void fire(NeoPixel * n)
{
    magenta(n);
    usleep(1000000);
    red(n);
    usleep(1000000);
    amber(n);
    usleep(1000000);
    // TODO: define function
}

//
// inputs: 
// outputs: 
void flagAmerican(NeoPixel * n)
{
    red(n);
    usleep(1000000);
    white(n);
    usleep(1000000);
    blue(n);
    usleep(1000000);
    // TODO: define function
}

//
// inputs: 
// outputs: 
void wild(NeoPixel * n)
{
    magenta(n);
    usleep(500000);
    red(n);
    usleep(500000);
    amber(n);
    usleep(500000);
    green(n);
    usleep(500000);
    teal(n);
    usleep(500000);
    blue(n);
    usleep(500000);
    // TODO: define function
}

// 
// inputs: none
// outputs: sends a bool to either keep the program alive or shutdown the system after 3 seconds
bool shutdownScript()
{
    for (int i = 0; i < 6; ++i)
    {
        // check every half second for shutdown script
        if (digitalRead(RESET) == 0)
            return false;
        usleep(500000);
    }
    return true;
}