//
// Created by Teo on 3/11/2021.
//

#include "Console.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
Console * createConsole(estateService * someEstateService)
/// This function is responsible for creating a new console
/// \param someEstateService - the estateService, part of the console
/// \return - the address of the newly created console
{
    Console * newConsole = (Console*)malloc(sizeof (Console));
    newConsole->theEstateService = someEstateService;
    return newConsole;
}

void destroyConsole(Console * someConsole)
/// This function is responsible for destroying a console
/// \param someConsole - the console we want to destroy
{
    destroyEstateService(someConsole->theEstateService);
    free(someConsole);
}

Estate * readEstate()
/// This function is responsible for reading the data for a new estate and creating a new estate
/// \return - The newly created estate
{
    char estateType[10];
    char estateAddress[256];
    readEstateType(estateType);
    readEstateAddress(estateAddress);
    int theEstateSurface = readEstateSurface();
    int theEstatePrice = readEstatePrice();
    Estate * newEstate = createEstate(estateType, estateAddress, theEstateSurface, theEstatePrice);
    return newEstate;
}

void readEstateAddress(char * estateAddress)
/// This function is responsible for reading an estate address
/// \param estateAddress - the address of the estate address
{
    printf("\nPlease enter the address of the estate!\n");
    printf("Estate address: ");
    scanf("%[^\n]", estateAddress);
    getchar();
    stringToUpper(estateAddress);
}

void readEstateType(char * estateType)
/// This function is responsible for reading an estate type. This function also makes sure that the estate type is a valid one
/// \param estateType - the address of the estate type
{
    printf("\nPlease enter the type of the estate!\n");
    printf("Estate type: ");
    scanf("%[^\n]", estateType);
    getchar();
    stringToUpper(estateType);
    while (strcmp(estateType, "HOUSE") != 0 && strcmp(estateType, "APARTMENT") != 0 &&
           strcmp(estateType, "PENTHOUSE") != 0) {
        printf("\nInvalid estate type! It should be house, apartment or penthouse! Please try again!\n");
        printf("Estate type: ");
        scanf("%[^\n]", estateType);
        getchar();
        stringToUpper(estateType);
    }
}

int readEstateSurface()
/// This function is responsible for reading the surface of an estate. This function also makes sure the estate surface is a valid one
/// \return - the surface
{
    char estateSurface[10];
    printf("\nPlease enter the surface of the estate!\n");
    printf("Estate surface: ");
    scanf("%[^\n]", estateSurface);
    getchar();
    int surface = strtol(estateSurface, NULL, 10);
    while (surface <= 0) {
        printf("\nInvalid estate surface! The estate surface should be and integer > 0! Please try again!\n");
        printf("Estate surface: ");
        scanf("%[^\n]", estateSurface);
        getchar();
        surface = strtol(estateSurface, NULL, 10);
    }
    return surface;
}

int readEstatePrice()
/// This function is responsible for reading the price of an estate. This function also makes sure the estate price is a valid one
/// \return - the price
{
    char estatePrice[10];
    printf("\nPlease enter the price of the estate!\n");
    printf("Estate price: ");
    scanf("%[^\n]", estatePrice);
    getchar();
    int price = strtol(estatePrice, NULL, 10);
    while (price <= 0) {
        printf("\nInvalid estate price! The estate price should be and integer > 0! Please try again!\n");
        printf("Estate price: ");
        scanf("%[^\n]", estatePrice);
        getchar();
        price = strtol(estatePrice, NULL, 10);
    }
}

void stringToUpper(char * someString)
/// This function is responsible for converting the lowercase letter from a string to uppercase letters
/// \param someString - the address of the string
{
    int index;
    for (index = 0; index < strlen(someString); index++) {
        if (someString[index] >= 'a' && someString[index] <='z') {
            someString[index] -= 32;
        }
    }
}

void addEstateUi(Console * someConsole)
/// This is responsible for adding a new estate
/// \param someConsole - console
{
    Estate * newEstate = readEstate();
    bool additionStatus = addEstateService(someConsole->theEstateService, newEstate);
    if (additionStatus) {
        printf("\nThe addition was successful!\n");
    }
    else
    {
        printf("\nThere is already an estate at that address!\n");
    }
}

void deleteEstateUi(Console * someConsole)
/// This is responsible for deleting an estate
/// \param someConsole - console
{
    if (someConsole->theEstateService->theEstateRepository->estatesList->length == 0) {
        printf("\nThere are no estates!\n");
    }
    else {
        char estateAddress[256];
        readEstateAddress(estateAddress);
        bool deletionStatus = removeEstateService(someConsole->theEstateService, estateAddress);
        if (deletionStatus) {
            printf("\nThe estate was deleted successfully!\n");
        } else {
            printf("\nThere is no estate at that address!\n");
        }
    }
}

void updateEstateUi(Console * someConsole)
/// This is responsible for updating an estate
/// \param someConsole - console
{
    if (someConsole->theEstateService->theEstateRepository->estatesList->length == 0) {
        printf("\nThere are no estates!\n");
    }
    else {
        Estate *updatedEstate = readEstate();
        bool updateStatus = updateEstateService(someConsole->theEstateService, updatedEstate);
        if (updateStatus) {
            printf("\nThe estate was updated successfully!\n");
        } else {
            printf("\nThere is no estate having that address!\n");
        }
    }
}

void listAllEstates(Console * someConsole)
/// This function is responsible for listing all the existing estates from the repository
/// \param someConsole - console
{
    if (someConsole->theEstateService->theEstateRepository->estatesList->length == 0) {
        printf("\nThere are no estates at the moment!\n");
    }
    else {
        listEstatesFromArray(someConsole->theEstateService->theEstateRepository->estatesList);
    }
}

void listEstatesFromArray(dynamicArray * someDynamicArray)
/// This function is responsible for listing all the estates from a dynamic array
/// \param someDynamicArray - the dynamic array which contains the estates we wanna print
{
    {
        int index;
        for (index = 0; index < someDynamicArray->length; index++) {
            Estate *printEstate = getElement(someDynamicArray, index);
            printf("The state at the address: %s, being a/n: %s, having the surface: %d, is being sold for: %d\n",
                   printEstate->estateAddress, printEstate->estateType, printEstate->estateSurface,
                   printEstate->estatePrice);
        }
    }
}

void filterEstates(Console * someConsole)
/// This function is responsible for calling the functions responsible for the filtering based on address and price
/// \param someConsole - console
{
    printf("\nOn what criteria do you want to perform the filter? Address or higher than a given price? Type address or price!\n");
    char option[10];
    scanf("%s", option);
    getchar();
    stringToUpper(option);
    if (strcmp(option, "ADDRESS") == 0) {
        listMatchingEstate(someConsole);
    } else if (strcmp(option, "PRICE") == 0) {
        listMatchingPrice(someConsole);
    }
    else {
        printf("\nINVALID FILTER OPTION!\n");
    }
}

void listMatchingEstate(Console * someConsole)
/// This function is responsible for the filtering based on the address
/// \param someConsole - console
{
    if (someConsole->theEstateService->theEstateRepository->estatesList->length == 0) {
        printf("\nThere are no estates at the moment!\n");
    }
    else {
        char addressToMatch[256];
        char option[10];
        printf("\nPlease enter the address based on which you want to filter!\n");
        fgets(addressToMatch, 255, stdin);
        stringToUpper(addressToMatch);
        addressToMatch[strlen(addressToMatch) -1] = '\0';
        printf("\nBased on what you want to perform the sort? Type either surface or price!\n");
        scanf("%s", option);
        getchar();
        stringToUpper(option);
        dynamicArray *matchingEstates = findAllMatchingEstates(someConsole->theEstateService, addressToMatch, option);
        if (matchingEstates->length == 0) {
            printf("\nThere are no matching estates!\n");
        } else {
            listEstatesFromArray(matchingEstates);
        }
        destroyDynamicArray(&matchingEstates);
    }
}

void listMatchingType(Console * someConsole)
/// This function is responsible for filtering the estates based on a given estate type and surface
/// \param someConsole - console
{
    if (someConsole->theEstateService->theEstateRepository->estatesList->length == 0) {
        printf("\nThere are no estates at the moment!\n");
    }
    else {
        char estateType[10];
        readEstateType(estateType);
        int estateSurface = readEstateSurface();
        char option[11];
        printf("\nHow do you want the sort to be? Ascending or descending?\n");
        scanf("%[^\n]", option);
        getchar();
        stringToUpper(option);
        dynamicArray *matchingEstates = findAllTypeEstates(someConsole->theEstateService, estateType, estateSurface, option);
        if (matchingEstates->length == 0) {
            printf("\nThere are no matching estates!\n");
        } else {
            listEstatesFromArray(matchingEstates);
        }
        destroyDynamicArray(&matchingEstates);
    }
}

void listMatchingPrice(Console * someConsole)
/// This function is responsible for filtering the estates based on a given price
/// \param someConsole - console
{
    if (someConsole->theEstateService->theEstateRepository->estatesList->length == 0) {
        printf("\nThere are no estates at the moment!\n");
    }
    else {
        int estatePrice = readEstatePrice();
        char option[11];
        printf("\nHow do you want the sort to be? Ascending or descending?\n");
        scanf("%[^\n]", option);
        getchar();
        stringToUpper(option);
        dynamicArray *matchingEstates = findPriceEstates(someConsole->theEstateService, estatePrice, option);
        if (matchingEstates->length == 0) {
            printf("\nThere are no matching estates!\n");
        } else {
            listEstatesFromArray(matchingEstates);
        }
        destroyDynamicArray(&matchingEstates);
    }
}

void undoOperation(Console * someConsole)
/// The function is responsible for undoing an operation
/// \param someConsole - console
{
    if (someConsole->theEstateService->theUndoOperations->repositoryRecordings->length == 0) {
        printf("\nThere are no operations to undone!\n");
    }
    else
    {
        undoSomeOperation(someConsole->theEstateService);
    }
}

void redoOperation(Console * someConsole)
/// This function is responsible for redoing an operation
/// \param someConsole - console
{
    if (someConsole->theEstateService->theRedoOperations->repositoryRecordings->length == 0) {
        printf("\nThere are no operations to redone!\n");
    }
    else
    {
        redoSomeOperation(someConsole->theEstateService);
    }
}

void printMenu()
///This funcion is responsible for printing the options of the program
{
    printf("\nThere are the available commands!\n"
           "add -  Add a new estate\n"
           "delete -  Delete an estate\n"
           "update -  Update an estate\n"
           "filter - Filters the estates based on address and sorts ascending base on a criteria\n"
           "type -  See all estates of a given type, having the surface greater than a provided value\n"
           "undo - Undo the last operation, if possible\n"
           "redo - Redo the last operation, if possible\n"
           "list - Displays all the existing estates\n"
           "exit -  Exit the application\n");
}

void runProgram(Console * someConsole)
/// This function is responsible for running the program
/// \param someConsole  - console
{
    printf("\nWelcome! It's free real estate!\n");
    char userCommand[10];
    while (1) {
        printMenu();
        printf("\nPlease enter your command!\n");
        scanf("%s", userCommand);
        getchar();
        if (strcmp(userCommand, "exit") == 0) {
            printf("\nWe had a good one! See you next time!\n");
            break;
        } else if (strcmp(userCommand, "add") ==0) {
            addEstateUi(someConsole);
        } else if (strcmp(userCommand, "delete") ==0) {
            deleteEstateUi(someConsole);
        } else if (strcmp(userCommand, "update") ==0) {
            updateEstateUi(someConsole);
        } else if (strcmp(userCommand, "list") == 0){
            listAllEstates(someConsole);
        } else if (strcmp(userCommand, "filter") == 0) {
            filterEstates(someConsole);
        } else if (strcmp(userCommand, "type") == 0) {
            listMatchingType(someConsole);
        } else if (strcmp(userCommand, "undo") == 0) {
            undoOperation(someConsole);
        } else if (strcmp(userCommand, "redo") == 0) {
            redoOperation(someConsole);
        } else
            printf("\nINVALID COMMAND!\n");
    }
    destroyConsole(someConsole);
}