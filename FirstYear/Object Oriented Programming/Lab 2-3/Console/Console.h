//
// Created by Teo on 3/11/2021.
//

#ifndef A23_ALEXTEO24_CONSOLE_H
#define A23_ALEXTEO24_CONSOLE_H
#include "../Service/Service.h"
typedef struct {
    estateService * theEstateService;
}Console;

Console * createConsole(estateService * someEstateService);

void listMatchingType(Console * someConsole);

void destroyConsole(Console * someConsole);

Estate * readEstate();

void runProgram(Console * someConsole);

void addEstateUi(Console * someConsole);

void deleteEstateUi(Console * someConsole);

void updateEstateUi(Console * someConsole);

void stringToUpper(char * someString);

void readEstateAddress(char * estateAddress);

void readEstateType(char * estateType);

int readEstateSurface();

int readEstatePrice();

void printMenu();

void listAllEstates(Console * someConsole);

void listMatchingEstate(Console * someConsole);

void listMatchingPrice(Console * someConsole);

void listEstatesFromArray(dynamicArray * someDynamicArray);

void filterEstates(Console * someConsole);

void undoOperation(Console * someConsole);

void redoOperation(Console * someConsole);

#endif //A23_ALEXTEO24_CONSOLE_H
