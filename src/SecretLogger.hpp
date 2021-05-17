/**
 * @file SecretLogger.hpp
 * @author Jacob H. Schandel (jacob.schandel@gmail.com)
 * @brief Header file for SecretLogger class
 * @version 0.1
 * @date 2021-05-17
 * 
 * @copyright Copyright (c) 2021
 * 
 */

#include <fstream>
#include <string>

class SecretLogger
{
public:
    /**
     * @brief Construct a new Logger object
     */
    SecretLogger();

    /**
     * @brief Log a message in the log file and std::cout
     * 
     * @param message info to log
     */
    void log(const std::string& message);

    ~SecretLogger();

private:
    std::string logFileName;

    /**
     * @brief file for error log
     */
    std::ofstream logFile;
};