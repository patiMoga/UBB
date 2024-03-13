cmake_minimum_required(VERSION 3.24)
project(Laborator4)

set(CMAKE_CXX_STANDARD 17)

add_executable(Laborator4 main.cpp patrat.cpp tests.cpp patrat.h tests.h repository.cpp repository.h operations.cpp operations.h)
