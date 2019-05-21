// Jacob H. Schandel
// boatlighting
// main.cpp

// Purpose: this file in the program is responsible for driving the rest of the program.

#include <iostream>
#include <wiringPi.h>

// Note: wiringPi.h is part of Raspbian, and may show as an error when writing code on a device not
//       Raspbian-based, such as a Windows PC code editor with debugging.

using namespace std;  // TODO: replace with proper usings.

// The following is the GPIO assignments for the project, defined as const ints:
//     Board Indicator RGB (optional): 2, 3, 4, for red, green, and blue, respectively
//     Red Relay for Exterior: 17
//     Green Relay for Exterior: 27
//     Blue Relay for Exterior: 22
//     Color Toggle: 21
//     Reset System Button: 20
//     Signal Pin for Interior: TBD

const int RGB_LED[3] = {2, 3, 4};
const int RGB_EXT[3] = {17, 27, 22};
const int RGB_INT_ADDR = -1;  // TODO: change to the chosen pin
const int TOGGLE = 21;
const int RESET = 20;