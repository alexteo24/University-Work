//
// Created by Teo on 4/12/2021.
//

#include <iostream>
#include "ConsoleUser.h"
#include <regex>
#include <iomanip>

ConsoleUser::ConsoleUser(ServiceUser &serviceUser) : _serviceUser{serviceUser} {}

void ConsoleUser::stringToUpper(std::string &someString)
{
    int index;
    for (index = 0; index < someString.length(); index++) {
        if (someString[index] >= 'a' and someString[index] <= 'z') {
            someString[index] -= 32;
        }
    }
}

int ConsoleUser::readInt() {
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

void ConsoleUser::readCoatSize(std::string &coatSize) {
    std::regex e ("[sml]{1}|[x]{1,3}[l]$", std::regex_constants::icase);
    std::cout<<"Please enter the size of the coat! It should be either S M L XL XXL XXXL!\n";
    getline(std::cin, coatSize);
    while (not((coatSize.length() != 0 and regex_match(coatSize, e) == 1) or coatSize.length() == 0)) {
        std::cout<<"Please enter the size of the coat! It should be either S M L XL XXL XXXL!\n";
        getline(std::cin, coatSize);
    }
    stringToUpper(coatSize);
}

void ConsoleUser::navigateOffers() {
    std::string size;
    std::string option;
    readCoatSize(size);
    _serviceUser.findMatchingSize(size);
    if (_serviceUser.anyMatchingCoats()) {
        std::cout<<"Currently, there are no coats matching the required size!\n";
    }
    else {
        bool next = false;
        Coat currentCoat = _serviceUser.nextItem();
        while (true) {
            unsigned int shoppingCartLength = _serviceUser.getCartForPrint().size();
            if (shoppingCartLength == 0) {
                std::cout << "\nYour cart is empty!\n";
            } else {
                std::cout << "\n\nYour shopping cart so far:\n\n";
                for (const Coat& c : _serviceUser.getCartForPrint()) {
                    std::cout<<std::left << std::setw(5) << c.getSize() << std::setw(15) <<
                             c.getColor() << std::setw(10) << c.getPrice() << std::setw(5)
                             << c.getQuantity() << std::setw(15) << c.getUniqueID() << std::setw(5)
                             << c.getPhotographLink() << '\n';
                }
            }
            std::cout << "\nCurrent coat:\n";
            if (next) {
                currentCoat = _serviceUser.nextItem();
                next = false;
            }
            std::cout<<std::left << std::setw(5) << currentCoat.getSize() << std::setw(15)
                     << currentCoat.getColor() << std::setw(10) << currentCoat.getPrice() << std::setw(5)
                     << currentCoat.getQuantity() << std::setw(15) << currentCoat.getUniqueID() << std::setw(5)
                     << currentCoat.getPhotographLink() << '\n';
            std::cout << "\nWhat do you want to do? Next, buy, cost, menu?\n";
            std::cout << "Please enter your option\n";
            getline(std::cin, option);
            stringToUpper(option);
            if (option == "BUY") {
                int amount;
                std::cout << "\nHow many coats do you want to buy?\n";
                amount = readInt();
                try {
                    _serviceUser.addToCart(currentCoat, amount);
                } catch (ShoppingException& se) {
                    std::cout<<se.what();
                }
            } else if (option == "NEXT") {
                next = true;
            } else if (option == "COST") {
                std::cout << "\nCurrent amount to pay: " << _serviceUser.computeCost() << '\n';
            } else if (option == "MENU") {
                break;
            }
        }
    }

}

void ConsoleUser::checkOut() {
    _serviceUser.checkOut();
}

void ConsoleUser::runConsole() {
    std::cout<<"Welcome to the shop!\n";
    std::string userCommand;
    while (true) {
        std::cout<<"Available commands!\n"
                   "offers - Navigate the offerings\n"
                   "checkout - Buying the content of the cart\n"
                   "shopping basket - Display the content of the cart\n"
                   "exit - Exits user mode\n";
        std::cout<<"Please enter your command!\n";
        getline(std::cin, userCommand);
        if (userCommand == "exit") {
            std::cout<<"Exiting user mode...\n";
            return;
        } else if (userCommand == "offers") {
            navigateOffers();
        } else if (userCommand == "checkout") {
            checkOut();
        } else if (userCommand == "shopping basket") {
            _serviceUser.write();
            _serviceUser.open();
        } else {
            std::cout<<"INVALID COMMAND!!!\n";
        }
    }
}

ConsoleUser::~ConsoleUser() = default;
