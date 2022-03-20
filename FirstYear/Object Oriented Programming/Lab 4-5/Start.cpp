//
// Created by Teo on 3/16/2021.
//
#include "ConsoleAdmin/ConsoleAdmin.h"
#include <iostream>
#include "ConsoleUser/ConsoleUser.h"
#include "Coat/TestCoat.h"
#include "DynamicArray/TestDynamicArray.h"
#include "RepositoryCoats/TestRepositoryCoats.h"
#include "RepositoryShopping/TestRepositoryShopping.h"
#include "ServiceAdmin/TestServiceAdmin.h"
#include "ServiceUser/TestServiceUser.h"

int main() {
    testCoat();
    testDynamicArray();
    testRepositoryCoats();
    testRepositoryShopping();
    testServiceAdmin();
    testServiceUser();
    RepositoryCoats repositoryCoats{10};
    repositoryCoats.initRepository();
    ServiceAdministrator serviceAdministrator{repositoryCoats};
    ConsoleAdmin consoleAdmin{serviceAdministrator};
    RepositoryShopping repositoryShopping;
    ServiceUser serviceUser{repositoryShopping, repositoryCoats};
    ConsoleUser consoleUser{serviceUser};
    std::string choice;
    bool areWeDone = false;
    while (not areWeDone) {
        std::cout << "How do you want to start the program?\n"
                     "1. Administrator mode\n"
                     "2. User mode\n"
                     "0. Exit\n"
                     "Please enter your command!\n";
        getline(std::cin, choice);
        if (choice == "1") {
            areWeDone = consoleAdmin.runProgramAdmin();
        }
        else if (choice == "2") {
            areWeDone = consoleUser.runProgram();
        } else if (choice == "0") {
            std::cout<<"Goodbye!";
            break;
        } else {
            std::cout<<"INVALID COMMAND!!!";
        }
    }
    return 0;
}