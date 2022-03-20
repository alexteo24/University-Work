cmake_minimum_required(VERSION 3.20)
project(Lab_4_5)

set(CMAKE_CXX_STANDARD 14)

add_executable(Lab_4_5 Start.cpp
        Coat/Coat.cpp
        Coat/Coat.h
        Coat/TestCoat.cpp
        Coat/TestCoat.h
        ConsoleAdmin/ConsoleAdmin.cpp
        ConsoleAdmin/ConsoleAdmin.h
        ConsoleUser/ConsoleUser.cpp
        ConsoleUser/ConsoleUser.h
        DynamicArray/DynamicArray.h
        DynamicArray/TestDynamicArray.cpp
        DynamicArray/TestDynamicArray.h
        RepositoryCoats/RepositoryCoats.cpp
        RepositoryCoats/RepositoryCoats.h
        RepositoryCoats/TestRepositoryCoats.cpp
        RepositoryCoats/TestRepositoryCoats.h
        RepositoryShopping/RepositoryShopping.cpp
        RepositoryShopping/RepositoryShopping.h
        RepositoryShopping/TestRepositoryShopping.cpp
        RepositoryShopping/TestRepositoryShopping.h
        ServiceAdmin/ServiceAdmin.cpp
        ServiceAdmin/ServiceAdmin.h
        ServiceAdmin/TestServiceAdmin.cpp
        ServiceAdmin/TestServiceAdmin.h
        ServiceUser/ServiceUser.cpp
        ServiceUser/ServiceUser.h
        ServiceUser/TestServiceUser.cpp
        ServiceUser/TestServiceUser.h)
