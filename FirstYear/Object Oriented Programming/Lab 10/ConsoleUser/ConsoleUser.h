//
// Created by Teo on 4/12/2021.
//

#ifndef REDONICE_CONSOLEUSER_H
#define REDONICE_CONSOLEUSER_H

#include "../ServiceUser/ServiceUser.h"

class ConsoleUser{
private:
    ServiceUser& _serviceUser;

public:
    ConsoleUser(ServiceUser& serviceUser);

    ~ConsoleUser();

    void runConsole();

    void readCoatSize(std::string &coatSize);

    void stringToUpper(std::string &someString);

    int readInt();

    void navigateOffers();

    void checkOut();
};

#endif //REDONICE_CONSOLEUSER_H
