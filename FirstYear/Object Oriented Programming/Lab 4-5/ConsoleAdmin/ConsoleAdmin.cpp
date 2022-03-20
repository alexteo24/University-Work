//
// Created by Teo on 3/17/2021.
//

#include "ConsoleAdmin.h"
#include <iostream>
#include <regex>

ConsoleAdmin::ConsoleAdmin(ServiceAdministrator &serviceAdministrator): serviceAdministrator{serviceAdministrator}{}

ConsoleAdmin::~ConsoleAdmin() = default;

bool ConsoleAdmin::stringToUpper(std::string &someString)
{
    int index;
    for (index = 0; index < someString.length(); index++) {
        if (isalpha(someString[index])) {
            if (someString[index] >= 'a' and someString[index] <= 'z') {
                someString[index] -= 32;
            }
        } else {
            return false;
        }
    }
    return true;
}

void ConsoleAdmin::readCoatID(std::string &coatID) {
    std::cout<<"Please enter and ID for the coat! It should have exactly 7 characters, letters only!\n";
    getline(std::cin, coatID);
    while(coatID.length() != 7 or not stringToUpper(coatID)) {
        std::cout<<"Please enter and ID for the coat! It should have exactly 7 characters, letters only!\n";
        getline(std::cin, coatID);
    }
}

void ConsoleAdmin::readCoatColor(std::string &coatColor) {
    std::cout<<"Please enter the color of the coat! It should have letters only!\n";
    getline(std::cin, coatColor);
    while(coatColor.length() == 0 or not stringToUpper(coatColor)) {
        std::cout<<"Please enter the color of the coat! It should have letters only!\n";
        getline(std::cin, coatColor);
    }
}

void ConsoleAdmin::readCoatPrice(int &coatPrice) {
    std::string stringPrice;
    std::cout<<"Please enter the price of the coat! It should be an integer number greater than 0!\n";
    getline(std::cin, stringPrice);
    while (stringPrice.length() == 0 or isalpha(stringPrice[0]) or stoi(stringPrice) <= 0) {
        std::cout<<"Please enter the price of the coat! It should be an integer number greater than 0!\n";
        getline(std::cin, stringPrice);
    }
    coatPrice = stoi(stringPrice);
}

void ConsoleAdmin::readCoatSize(std::string &coatSize) {
    std::regex e ("[sml]{1}|[x]{1,3}[l]$", std::regex_constants::icase);
    std::cout<<"Please enter the size of the coat! It should be either S M L XL XXL XXXL!\n";
    getline(std::cin, coatSize);
    while (coatSize.length() == 0 or regex_match(coatSize, e) == 0) {
        std::cout<<"Please enter the size of the coat! It should be either S M L XL XXL XXXL!\n";
        getline(std::cin, coatSize);
    }
    stringToUpper(coatSize);
}

void ConsoleAdmin::readCoatQuantity(int &quantity) {
    std::string stringQuantity;
    std::cout<<"Please enter the number of the coats! It should be an positive integer!\n";
    getline(std::cin, stringQuantity);
    while(stringQuantity.length() == 0 or isalpha(stringQuantity[0]) or stoi(stringQuantity) < 0) {
        std::cout<<"Please enter the number of the coats! It should be an positive integer!\n";
        getline(std::cin, stringQuantity);
    }
    quantity = stoi(stringQuantity);
}

void ConsoleAdmin::readCoatPhotographLink(std::string &photographLink) {
    std::regex e ("^https://www\\.[a-z]+\\.[a-z]{2,3}$", std::regex_constants::icase);
    std::cout<<"Please provide the link for the image of the coat!\n";
    getline(std::cin, photographLink);
    while (photographLink.length() == 0 or regex_match(photographLink, e) == 0) {
        std::cout<<"Please provide the link for the image of the coat!\n";
        getline(std::cin, photographLink);
    }
    //Perhaps some validation?
}

Coat ConsoleAdmin::readCoatData() {
    std::string size;
    std::string color;
    int price;
    int quantity;
    std::string photographLink;
    std::string uniqueID;
    readCoatSize(size);
    readCoatColor(color);
    readCoatPrice(price);
    readCoatQuantity(quantity);
    readCoatPhotographLink(photographLink);
    readCoatID(uniqueID);
    Coat newCoat = Coat(size, color, price, quantity, photographLink, uniqueID);
    return newCoat;
}

void ConsoleAdmin::addCoatUI() {
    Coat newCoat = readCoatData();
    bool additionStatus = this->serviceAdministrator.addNewCoatService(newCoat);
    if (additionStatus) {
        std::cout<<"The addition was successful!\n";
    } else {
        std::cout<<"There already is a coat having the same ID!\n";
        //perhaps destroy the new coat? In the service, but reminder here
    }
}

void ConsoleAdmin::updateCoatUI() {
    Coat updatedCoat = readCoatData();
    bool updateStatus = this->serviceAdministrator.updateCoatService(updatedCoat);
    if (updateStatus) {
        std::cout<<"The update was successful!\n";
        // destroy the coat to be updated
    } else {
        std::cout<<"There is no coat having that ID!\n";
        // destroy the new coat
    }
}

void ConsoleAdmin::deleteCoatUI() {
    std::string coatID;
    readCoatID(coatID);
    bool deletionStatus = this->serviceAdministrator.deleteCoatService(coatID);
    if (deletionStatus) {
        std::cout<<"The delete was successful!\n";
        // destroy deleted coat
    } else {
        std::cout<<"There is no coat having that ID or the coat was not sold out!\n";
    }
}

void ConsoleAdmin::printAllCoats() {
    int nrCoats = this->serviceAdministrator.getRepository().getDynamicArray().getLength();
    int index;
    for (index = 0; index < nrCoats; index++) {
//        Coat coat = serviceAdministrator.getRepository().getDynamicArray()[index];
//        std::cout<<"The coat <insert link here> having the ID: "<<printCoat->getUniqueID()<<" has: the size: "<<
//        printCoat->getSize()<<"; the color: "<<printCoat->getColour()<<"; the price: "<<
//        printCoat->getPrice()<<"; and a stock of: "<<printCoat->getQuantity()<<"\n";
        std::cout<<serviceAdministrator.getRepository().getDynamicArray()[index];
    }
}

void ConsoleAdmin::printCommands() {
    std::cout<<"Admin mode engaged!\n"
          "add - Add new coat\n"
          "update - Update an already existing coat details\n"
          "delete - Delete a coat\n"
          "list - Prints all the coats\n"
          "user - Switch to user mode\n"
          "exit - Exit the app\n";
}

bool ConsoleAdmin::runProgramAdmin() {
    std::string userCommand;
    while (true) {
        printCommands();
        std::cout<<"Please enter your command!\n";
        getline(std::cin, userCommand);
        stringToUpper(userCommand);
        if (userCommand == "EXIT") {
            std::cout<<"Goodbye sir!\n";
            return true;
        } else if (userCommand == "ADD") {
            addCoatUI();
        } else if (userCommand == "UPDATE") {
            updateCoatUI();
        } else if (userCommand == "DELETE") {
            deleteCoatUI();
        } else if (userCommand == "USER") {
            return false;
        } else if (userCommand == "LIST") {
            printAllCoats();
        } else {
            std::cout<<"INVALID COMMAND!!!\n";
        }
    }
}
