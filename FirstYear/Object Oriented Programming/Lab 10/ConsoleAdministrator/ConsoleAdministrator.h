//
// Created by Teo on 3/31/2021.
//
#pragma once
#ifndef REDONICE_CONSOLEADMINISTRATOR_H
#define REDONICE_CONSOLEADMINISTRATOR_H


#include "../ServiceAdmin/ServiceAdministrator.h"

class ConsoleAdministrator {
private:
    ServiceAdministrator& _serviceAdmin;

public:
    ConsoleAdministrator(ServiceAdministrator& serviceAdmin);

    ~ConsoleAdministrator();

    static void stringToUpper(std::string &_string);

    void addCoatUI();

    void runConsole();

    void deleteCoatUI();

    void updateCoatUI();

    void printCoats();

    void readCoat(std::string& size, std::string& color, std::string& uniqueID, std::string& photographLink, int &price, int &quantity);

    int readInt();

    static void printCommands();
};


#endif //REDONICE_CONSOLEADMINISTRATOR_H
