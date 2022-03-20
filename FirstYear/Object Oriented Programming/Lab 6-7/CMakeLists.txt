cmake_minimum_required(VERSION 3.20)
project(Lab_6_7)

set(CMAKE_CXX_STANDARD 14)

add_executable(Lab_6_7 main.cpp
        ConsoleAdministrator/ConsoleAdministrator.cpp
        ConsoleAdministrator/ConsoleAdministrator.h
        ConsoleUser/ConsoleUser.cpp
        ConsoleUser/ConsoleUser.h
        Domain/Coat.cpp
        Domain/Coat.h
        RepositoryCoats/ExceptionsRepoCoats.cpp
        RepositoryCoats/ExceptionsRepoCoats.h
        RepositoryCoats/RepositoryCoats.cpp
        RepositoryCoats/RepositoryCoats.h
        RepositoryCoats/RepositoryCoatsFile.cpp
        RepositoryCoats/RepositoryCoatsFile.h
        RepositoryShopping/RepostioryShopping.cpp
        RepositoryShopping/RepostioryShopping.h
        ServiceAdmin/ServiceAdministrator.cpp
        ServiceAdmin/ServiceAdministrator.h
        ServiceUser/ServiceUser.cpp
        ServiceUser/ServiceUser.h
        ServiceUser/ShoppingExceptions.cpp
        ServiceUser/ShoppingExceptions.h
        Validators/ValidatorCoat.cpp
        Validators/ValidatorCoat.h)
