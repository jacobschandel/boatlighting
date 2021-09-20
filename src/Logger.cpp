/**
 * @file SecretLogger.hpp
 * @author Jacob H. Schandel (jacob.schandel@gmail.com)
 * @brief Implementation file for SecretLogger class
 * @version 0.1
 * @date 2021-05-17
 * 
 * @copyright Copyright (c) 2021
 * 
 */

#include "Logger.hpp"
#include <iostream>

Logger::Logger()
{
    logFileName = "boatlights.log";

    // new log file
    logFile.open(logFileName, std::ofstream::out);  
}

void Logger::log(const std::string& message)
{
    std::cout << message << std::endl;
    logFile << message << std::endl;
}

Logger::~Logger()
{
    logFile.close();
}