cmake_minimum_required(VERSION 3.16)
project(DSA_Problem_26_Lab3)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(DSA_Problem_26_Lab3
        App.cpp
        ExtendedTest.cpp
        ExtendedTest.h
        IteratedList.cpp
        IteratedList.h
        ListIterator.cpp
        ListIterator.h
        ShortTest.cpp
        ShortTest.h)
