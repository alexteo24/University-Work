#include <iostream>
#include "RepositoryCoats/RepositoryCoats.h"
#include "RepositoryCoats/RepositoryCoatsFile.h"
#include "RepositoryShopping/RepostioryShopping.h"
#include "ServiceAdmin/ServiceAdministrator.h"
#include "ServiceUser/ServiceUser.h"
#include "ConsoleAdministrator/ConsoleAdministrator.h"
#include "ConsoleUser/ConsoleUser.h"

int main() {
    RepositoryCoatsFile repoCoatsFile;
    ServiceAdministrator serviceAdmin{repoCoatsFile};
    ConsoleAdministrator consoleAdmin{serviceAdmin};
    std::string option;
    RepositoryShopping *repositoryShopping;
    std::cout<<"Please choose the type of file you want to use! (html or csv)\n";
    getline(std::cin, option);
    while(option != "csv" && option != "html") {
        std::cout<<"Please enter a valid type!\n";
        getline(std::cin, option);
    }
    if (option == "html") {
        repositoryShopping = new HTMLAdoptionList();
    } else {
        repositoryShopping = new CSVAdoptionList();
    }
    ServiceUser serviceUser{repoCoatsFile, repositoryShopping};
    ConsoleUser consoleUser{serviceUser};
    std::string choice;
    bool areWeDoneYet = false;
    while (!areWeDoneYet) {
        std::cout<<"How do you wanna start the program?\n"
                   "1. Admin mode\n"
                   "2. User mode\n"
                   "0. Exit program\n";
        std::cout<<"Please enter your option!\n";
        getline(std::cin, choice);
        if (choice == "0") {
            areWeDoneYet = true;
            std::cout<<"Bye bye!\n";
        } else if (choice == "1") {
            consoleAdmin.runConsole();
        } else if (choice == "2") {
            consoleUser.runConsole();
        } else {
            std::cout<<"INVALID COMMAND!\n";
        }
    }
    return 0;
}
