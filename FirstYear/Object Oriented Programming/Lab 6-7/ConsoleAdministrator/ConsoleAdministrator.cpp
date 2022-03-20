//
// Created by Teo on 3/31/2021.
//

#include "ConsoleAdministrator.h"
#include <iostream>
#include <iomanip>

ConsoleAdministrator::ConsoleAdministrator(ServiceAdministrator &serviceAdmin):_serviceAdmin(serviceAdmin){}

ConsoleAdministrator::~ConsoleAdministrator() = default;

void ConsoleAdministrator::printCommands() {
    std::cout<<"Available commands!\n"
               "add - Add new coat\n"
               "update - Update an already existing coat details\n"
               "delete - Delete a coat\n"
               "list - Prints all the coats\n"
               "user - Switch to user mode\n"
               "exit - Exit the app\n";
}

void ConsoleAdministrator::stringToUpper(std::string &_string) {
    int index;
    for (index = 0; index < _string.length(); index++) {
        if (_string[index] >= 'a' && _string[index] <= 'z') {
            _string[index] -= 32;
        }
    }
}

int ConsoleAdministrator::readInt() {
    int value;
    while(!(std::cin >> value)) {
        std::cin.clear();
        while (std::cin.get() != '\n') {
            continue;
        }
        std::cout << "Please enter a valid integer!\n";
    }
    return value;
}

void ConsoleAdministrator::readCoat(std::string &size, std::string &color, std::string &uniqueID,
                                    std::string &photographLink, int &price, int &quantity) {
    std::cout<<"Please enter the size of the coat! It should be either S M L XL XXL XXXL!\n";
    getline(std::cin, size);
    stringToUpper(size);
    std::cout<<"Please enter the color of the coat!\n";
    getline(std::cin, color);
    stringToUpper(color);
    std::cout<<"Please enter the uniqueID of the coat! It should be 7 characters long!\n";
    getline(std::cin, uniqueID);
    stringToUpper(uniqueID);
    std::cout<<"Please enter the link to the photograph of the coat! Ex: https://www.example.ex \n";
    getline(std::cin, photographLink);
    std::cout<<"Please enter the price of the coat!\n";
    price = readInt();
    std::cout<<"Please enter the quantity!\n";
    quantity = readInt();
}

void ConsoleAdministrator::addCoatUI() {
    std::string size;
    std::string color;
    std::string uniqueID;
    std::string photographLink;
    int price;
    int quantity;
    readCoat(size, color, uniqueID, photographLink, price, quantity);
    _serviceAdmin.addCoatService(size, color, uniqueID, photographLink, price, quantity);
}

void ConsoleAdministrator::deleteCoatUI() {
    std::string coatID;
    std::cout<<"Please enter the id of the coat you want to delete!\n";
    getline(std::cin, coatID);
    stringToUpper(coatID);
    _serviceAdmin.deleteCoatService(coatID);
}

void ConsoleAdministrator::updateCoatUI() {
    std::string size;
    std::string color;
    std::string uniqueID;
    std::string photographLink;
    int price;
    int quantity;
    readCoat(size, color, uniqueID, photographLink, price, quantity);
    _serviceAdmin.updateCoatService(size, color, uniqueID, photographLink, price, quantity);
}

void ConsoleAdministrator::printCoats() {
    std::vector<Coat> coatsList = _serviceAdmin.getCoatList();
    if (coatsList.empty()) {
        std::cout<<"Currently, there are no coats available!\n";
    } else {
        int index;
        for (index = 0; index < coatsList.size(); index++) {
            std::cout<<std::left << std::setw(5) << coatsList[index].getSize() << std::setw(15) <<
            coatsList[index].getColor() << std::setw(10) << coatsList[index].getPrice() << std::setw(5)
            << coatsList[index].getQuantity() << std::setw(15) << coatsList[index].getUniqueID() << std::setw(5)
            << coatsList[index].getPhotographLink() << '\n';
        }
    }
}

void ConsoleAdministrator::runConsole() {
    std::string userCommand;
    std::cout<<"Admin mode engaged!\n";
    while (true)
        try {
        printCommands();
        std::cout << "Enter your command!\n>>>";
        getline(std::cin, userCommand);
        if (userCommand == "exit") {
            std::cout<<"Bye bye!\n";
            return;
        } else if (userCommand == "add") {
            addCoatUI();
        } else if (userCommand == "delete") {
            deleteCoatUI();
        } else if (userCommand == "update") {
            updateCoatUI();
        } else if (userCommand == "list") {
            printCoats();
        } else {
            std::cout<<"INVALID COMMAND!\n";
        }
    } catch (std::exception& ex) {
            std::cout<<ex.what();
        }
}

