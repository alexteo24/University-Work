//
// Created by Teo on 3/25/2021.
//

#include "ConsoleUser.h"
#include <iostream>
#include <regex>

ConsoleUser::ConsoleUser(ServiceUser &serviceUser):serviceUser(serviceUser) {}

bool ConsoleUser::stringToUpper(std::string &someString)
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
    dynamicArray<Coat> matching = serviceUser.findMatchingSize(size);
    if (matching.getLength() == 0) {
        std::cout<<"There are no coats having that size!!!\n";
    }
    else {
        bool next = true;
        Coat currentCoat;
        while (true) {
            int shoppingCartLength = serviceUser.getCartForPrint().getLength();
            if (shoppingCartLength == 0) {
                std::cout << "\nYour cart is empty!\n";
            } else {
                std::cout << "\n\nYour shopping cart so far:\n\n";
                for (int index = 0; index < serviceUser.getCartForPrint().getLength(); index++) {
                    std::cout << serviceUser.getCartForPrint()[index] << '\n';
                }
            }
            std::cout << "\nCurrent coat:\n";
            if (next) {
                currentCoat = serviceUser.nextItem(matching);
                next = false;
            }
            std::cout << '\n' << currentCoat << '\n';
//            std::string open = "start " + currentCoat.getPhotographLink();
//            system(open.c_str());
            std::cout << "\nWhat do you want to do? Next, buy, cost, menu?\n";
            std::cout << "Please enter your option\n";
            getline(std::cin, option);
            stringToUpper(option);
            if (option == "BUY") {
                std::string amount;
                std::cout << "\nHow many coats do you want to buy?\n";
                getline(std::cin, amount);
                while (amount.length() == 0 or isalpha(amount[0]) or stoi(amount) <= 0) {
                    std::cout << "\nHow many coats do you want to buy?\n";
                    getline(std::cin, amount);
                }
                int actualAmount = stoi(amount);
                std::cout << serviceUser.addToCart(currentCoat, actualAmount, matching);
            } else if (option == "NEXT") {
                next = true;
            } else if (option == "COST") {
                std::cout << "\nCurrent amount to pay: " << serviceUser.computeCost() << '\n';
            } else if (option == "MENU") {
                break;
            }
        }
    }

}

void ConsoleUser::checkOut() {
    serviceUser.checkOut();
}

bool ConsoleUser::runProgram() {
    std::cout<<"Welcome to the shop!\n";
    std::string userCommand;
    while (true) {
        std::cout<<"Available commands!\n"
                   "offers - Navigate the offerings\n"
                   "admin - Switch to admin mode\n"
                   "checkout - Buying the content of the cart\n"
                   "exit - Exit the app\n";
        std::cout<<"Please enter your command!\n";
        getline(std::cin, userCommand);
        stringToUpper(userCommand);
        if (userCommand == "EXIT") {
            std::cout<<"Goodbye!\n";
            return true;
        } else if (userCommand == "OFFERS") {
            navigateOffers();
        } else if (userCommand == "ADMIN") {
            return false;
        } else if (userCommand == "CHECKOUT") {
            checkOut();
        } else {
            std::cout<<"INVALID COMMAND!!!\n";
        }
    }
}

ConsoleUser::~ConsoleUser() = default;



