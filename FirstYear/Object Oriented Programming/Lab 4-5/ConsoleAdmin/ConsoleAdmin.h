//
// Created by Teo on 3/17/2021.
//
#pragma once
#ifndef A45_ALEXTEO24_CONSOLEADMIN_H
#define A45_ALEXTEO24_CONSOLEADMIN_H
#include "../ServiceAdmin/ServiceAdmin.h"
class ConsoleAdmin {
private:
    ServiceAdministrator& serviceAdministrator;

public:
    ConsoleAdmin(ServiceAdministrator &serviceAdministrator);

    ~ConsoleAdmin();

    bool runProgramAdmin();

private:
    static bool stringToUpper(std::string &someString);

    /// Reading a coatID
    /// \param coatID - address of the coat id
    void readCoatID(std::string &coatID);

    /// Reading a coat color
    /// \param coatColor - address of the coat color
    void readCoatColor(std::string &coatColor);

    /// Reading a coat price
    /// \param coatPrice - address of the coat price
    void readCoatPrice(int &coatPrice);

    /// Reading a coat size
    /// \param coatSize - address of the coat size
    void readCoatSize(std::string &coatSize);

    /// Reading a coat quantity
    /// \param quantity - address of the coat quantity
    void readCoatQuantity(int &quantity);

    /// Reading a photograph link
    /// \param photographLink - address of the coat photograph link
    void readCoatPhotographLink(std::string &photographLink);

    /// Reading the data for creating a coat
    /// \return - the newly created coat
    Coat readCoatData();

    /// UI for adding a coat
    void addCoatUI();

    /// UI for updating a coat
    void updateCoatUI();

    /// UI for deleting a coat
    void deleteCoatUI();

    /// Printing the menu
    static void printCommands();

    /// Printing all the coats
    void printAllCoats();

};

#endif //A45_ALEXTEO24_CONSOLEADMIN_H
