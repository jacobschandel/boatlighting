/**
 * @file main.cpp
 * @author Jacob H. Schandel (jacob.schandel@gmail.com)
 * @brief main executable for lighting program
 * @version 2.0
 * @date 2021-05-17
 * 
 * @copyright Copyright (c) 2021
 * 
 */

#include "Logger.hpp"

#include <iostream>

/**
 * @brief Main function of new boatlighting program
 * 
 * @param argc number of arguments (may not exceed 2)
 * @param argv argument contents(first is ./boatlighting, then -[char for mode])
 * @return int status code
 */
int main (int argc, char** argv)
{
    // this program accepts only one argument: a mode of execution
    char mode;

    if (argc > 2)
        return -1;
    
    // retrieve a specified mode
    else if (argc == 2)
    {
        mode = argv[1][1];
    }

    // normal operation without args
    else mode = 'n';

    Logger logger;

    logger.log("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    logger.log("~       BOAT LIGHTING CONTROL SYSTEM       ~");
    logger.log("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");

    // TODO: define lighting systems
    // TODO: get connected data to app

    return 0;
}