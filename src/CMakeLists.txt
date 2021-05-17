# Can be run by any version of CMake >= this
cmake_minimum_required(VERSION 3.10)

# project info
project(boatlighting)

# C++17 standard
set(CMAKE_CXX_STANDARD 17)

# Use Release build type if not specified
if (NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# main program
set(MAIN_SOURCE main.cpp)
add_executable(boatlighting ${MAIN_SOURCE})

# Turn on warnings
if (MSVC)
    # warning level 4
    add_compile_options(/W4)
else()
    # standard warnings
    add_compile_options(-Wall)
endif()

# Demo run command
add_custom_target(run
        COMMENT "Run debugging mode for boatlighting"
        COMMAND ./boatlighting -d
        DEPENDS boatlighting
        USES_TERMINAL
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
)
