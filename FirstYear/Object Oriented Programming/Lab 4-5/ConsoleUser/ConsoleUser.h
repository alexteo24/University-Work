//
// Created by Teo on 3/25/2021.
//

#ifndef A45_ALEXTEO24_CONSOLEUSER_H
#define A45_ALEXTEO24_CONSOLEUSER_H
#include "../ServiceUser/ServiceUser.h"

class ConsoleUser {

private:
    ServiceUser& serviceUser;

public:
    ConsoleUser(ServiceUser& serviceUser);

    ~ConsoleUser();

    /// Navigating and deciding what to do for each offer
    void navigateOffers();

    /// Running the console
    bool runProgram();

    /// Getting a string from lower to uppercase
    /// \param someString - the address of the string
    /// \return - true if the sting contains only letters, false otherwise
    static bool stringToUpper(std::string &someString);

    /// Reading a coat size
    /// \param coatSize - the address of the coat size
    void readCoatSize(std::string &coatSize);

    /// UI checkout
    void checkOut();
};
#endif //A45_ALEXTEO24_CONSOLEUSER_H
