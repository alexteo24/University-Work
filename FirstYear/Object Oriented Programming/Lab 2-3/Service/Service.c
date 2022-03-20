//
// Created by Teo on 3/11/2021.
//

#include "Service.h"
#include <stdlib.h>
#include <string.h>
estateService * createEstateService(estateRepository * someEstateRepository)
/// This function is responsible for creating an instance of estateService
/// \param someEstateRepository - the estateRepository
/// \return - the address of the newly created estate service
{
    estateService * theEstateService = (estateService*)malloc(sizeof (estateService));
    theEstateService->theEstateRepository = someEstateRepository;
    theEstateService->theRedoOperations = createRedo();
    theEstateService->theUndoOperations = createUndo();
    return theEstateService;
}

void destroyEstateService(estateService * someEstateService)
/// This function is responsible for properly destroying an estateService
/// \param someEstateService - the estate service we want to destroy
{
    destroyEstateRepository(someEstateService->theEstateRepository);
    destroyRedoOperations(someEstateService->theRedoOperations);
    destroyUndoOperations(someEstateService->theUndoOperations);
    free(someEstateService);
}

bool addEstateService(estateService * someEstateService, Estate * newEstate)
/// This function is responsible for adding a new estate
/// \param someEstateService - estate service containing the repository to which we want to add
/// \param newEstate - the estate we want to add
/// \return - True if there is no estate at the address of the new estate and the addition was successful, false otherwise
{
    if (someEstateService->theEstateRepository->estatesList->length == 0) {
        addUndoOperation(someEstateService->theUndoOperations, (TElem *) copyEstateRepository(someEstateService->theEstateRepository));
        addEstate(someEstateService->theEstateRepository, newEstate);
        return true;
    }
    else {
        int estatePosition = findEstate(someEstateService->theEstateRepository, newEstate->estateAddress);
        if (estatePosition != -1) {
            destroyEstate(newEstate);
            return false;
        } else {
            addUndoOperation(someEstateService->theUndoOperations, (TElem *) copyEstateRepository(someEstateService->theEstateRepository));
            addEstate(someEstateService->theEstateRepository, newEstate);
            return true;
        }
    }
}

bool removeEstateService(estateService * someEstateService, char* estateAddress)
/// This function is responsible for removing the estate matching the given address
/// \param someEstateService - estate service containing the repository from which we want to remove an estate
/// \param estateAddress - the address of the estate we want to remove
/// \return - True if the address exists and the remove is successful, false otherwise
{
    if (someEstateService->theEstateRepository->estatesList->length == 0) {
        return false;
    }
    else {
        int estatePosition = findEstate(someEstateService->theEstateRepository, estateAddress);
        if (estatePosition == -1) {
            return false;
        } else {
            addUndoOperation(someEstateService->theUndoOperations, (TElem *) copyEstateRepository(someEstateService->theEstateRepository));
            removeEstate(someEstateService->theEstateRepository, estateAddress);
            return true;
        }
    }
}

bool updateEstateService(estateService * someEstateService, Estate * updatedEstate)
/// This function is responsible for updating the estate found at the address of updatedEstate
/// \param someEstateService - estate service containing the repository in which we want to update an estate
/// \param updatedEstate - the already updated estate
/// \return - True if there exists an estate having the same address as updatedEstate and the update is successful, false otherwise
{
    if (someEstateService->theEstateRepository->estatesList->length == 0) {
        return false;
    }
    else {
        int estatePosition = findEstate(someEstateService->theEstateRepository, updatedEstate->estateAddress);
        if (estatePosition == -1) {
            destroyEstate(updatedEstate);
            return false;
        } else {
            addUndoOperation(someEstateService->theUndoOperations, (TElem *) copyEstateRepository(someEstateService->theEstateRepository));
            updateEstate(someEstateService->theEstateRepository, updatedEstate);
            return true;
        }
    }
}

int comparePriceAscending (Estate * a, Estate * b)
{
    return a->estatePrice > b->estatePrice;
}

int comparePriceDescending (Estate * a, Estate * b)
{
    return a->estatePrice < b->estatePrice;
}

int compareSurfaceAscending (Estate * a, Estate * b)
{
    return a->estateSurface > b->estateSurface;
}

int compareSurfaceDescending (Estate * a, Estate * b)
{
    return a->estateSurface < b->estateSurface;
}

dynamicArray * findAllMatchingEstates(estateService * someEstateService, char * estatePartialAddress, char * option)
/// This function is responsible for finding all the estates matching the estatePartialAddress and then sorting the
/// matching estates ascending, based on the option
/// \param someEstateService - estate service containing the repository
/// \param estatePartialAddress  - the address based on what we want to filter the repository
/// \param option - the option of the sort: either surface or price, otherwise no sorting will be performed
/// \return - the address of the dynamic array containing the filtered and sorted estates
{
    dynamicArray * listMatchingEstates = createDynamicArray(10);
    int (*criteria[])(Estate*, Estate*) = {compareSurfaceAscending, comparePriceAscending};
    int index;
    for (index = 0; index < someEstateService->theEstateRepository->estatesList->length; index++) {
        Estate * matchingEstate = someEstateService->theEstateRepository->estatesList->elements[index];
        if (strstr(matchingEstate->estateAddress, estatePartialAddress) != 0) {
            addElement(listMatchingEstates, matchingEstate);
        }
    }
    int choice;
    if (strcmp(option, "SURFACE") == 0) {
        choice = 0;
    } else if (strcmp(option, "PRICE") == 0) {
        choice = 1;
    } else {
        return listMatchingEstates;
    }
    int secondIndex;
    for (index = 0; index < listMatchingEstates->length - 1; index++) {
        for (secondIndex = index; secondIndex < listMatchingEstates->length; secondIndex++) {
            if ((criteria[choice]((getElement(listMatchingEstates, index)), getElement(listMatchingEstates, secondIndex)))) {
                Estate * auxiliaryEstate = getElement(listMatchingEstates, index);
                updateElement(listMatchingEstates, index, getElement(listMatchingEstates, secondIndex));
                updateElement(listMatchingEstates, secondIndex, auxiliaryEstate);
            }
        }
    }
    return listMatchingEstates;
}

dynamicArray * findPriceEstates(estateService * someEstateService, int estatePrice, char * option)
/// This function is responsible for finding all the estates having a price greater than a given price
/// \param someEstateService - estate service containing the repository
/// \param estatePrice - the price based on what we want to filter
/// \param option - the option of the sort: ascending or descending, no sort will be performed otherwise
/// \return - the address of the dynamic array containing the filtered and sorted estates
{
    dynamicArray *matchingArray = createDynamicArray(10);
    int (*criteria[])(Estate*, Estate*) = {comparePriceAscending, comparePriceDescending};
    int index;
    for (index = 0; index < someEstateService->theEstateRepository->estatesList->length; index++) {
        Estate * matchingEstate = someEstateService->theEstateRepository->estatesList->elements[index];
        if (matchingEstate->estatePrice > estatePrice) {
            addElement(matchingArray, matchingEstate);
        }
    }
    int choice = -1;
    if (strcmp(option, "ASCENDING") == 0) {
        choice = 0;
    } else if (strcmp(option, "DESCENDING") == 0) {
        choice = 1;
    }
    if (choice != -1) {
        int secondIndex;
        for (index = 0; index < matchingArray->length - 1; index++) {
            for (secondIndex = index; secondIndex < matchingArray->length; secondIndex++) {
                if ((criteria[choice]((getElement(matchingArray, index)), getElement(matchingArray, secondIndex)))) {
                    Estate * auxiliaryEstate =
                            getElement(matchingArray, index);
                    updateElement(matchingArray, index, getElement(matchingArray, secondIndex));
                    updateElement(matchingArray, secondIndex, auxiliaryEstate);
                }
            }
        }
    }
    return matchingArray;
}

dynamicArray * findAllTypeEstates(estateService * someEstateService, char *estateType, int estateSurface, char * option)
/// This function is responsible for filtering the estates having a given type and with a surface greater than a given surface
/// \param someEstateService - estate service containing the repository
/// \param estateType - the type of estate we want to filter: will always be house, apartment or penthouse
/// \param estateSurface - the surface based on what we want to filter
/// \param option - the option of the sort: ascending or descending, no sort will be performed otherwise
/// \return - the address of the dynamic array containing the filtered and sorted estates
{
    dynamicArray *matchingArray = createDynamicArray(10);
    int (*criteria[])(Estate*, Estate*) = {compareSurfaceAscending, compareSurfaceDescending};
    int nrElements = someEstateService->theEstateRepository->estatesList->length;
    int index;
    Estate * currentEstate = NULL;
    for (index = 0; index < nrElements; index++) {
        currentEstate = getElement(someEstateService->theEstateRepository->estatesList, index);
        if (strcmp(currentEstate->estateType, estateType) == 0 && currentEstate->estateSurface > estateSurface) {
            addElement(matchingArray, currentEstate);
        }
    }
    int choice = -1;
    if (strcmp(option, "ASCENDING") == 0) {
        choice = 0;
    } else if (strcmp(option, "DESCENDING") == 0) {
        choice = 1;
    }
    if (choice != -1) {
        int secondIndex;
        for (index = 0; index < matchingArray->length - 1; index++) {
            for (secondIndex = index; secondIndex < matchingArray->length; secondIndex++) {
                if ((criteria[choice]((getElement(matchingArray, index)), getElement(matchingArray, secondIndex)))) {
                    Estate * auxiliaryEstate = getElement(matchingArray, index);
                    updateElement(matchingArray, index, getElement(matchingArray, secondIndex));
                    updateElement(matchingArray, secondIndex, auxiliaryEstate);
                }
            }
        }
    }
    return matchingArray;
}

void undoSomeOperation(estateService * someEstateService)
/// This function is responsible for undoing an operation
/// \param someEstateService - service
{
    addRedoOperation(someEstateService->theRedoOperations,
                     (TElem *) copyEstateRepository(someEstateService->theEstateRepository));
    destroyEstateRepository(someEstateService->theEstateRepository);
    dynamicArray * repositoryRecordings = someEstateService->theUndoOperations->repositoryRecordings;
    someEstateService->theEstateRepository = repositoryRecordings->elements[repositoryRecordings->length - 1];
    deleteUndoOperation(someEstateService->theUndoOperations);
}

void redoSomeOperation(estateService * someEstateService)
/// This function is responsible for redoing an operation
/// \param someEstateService - service
{
    addUndoOperation(someEstateService->theUndoOperations,
                     (TElem *) copyEstateRepository(someEstateService->theEstateRepository));
    destroyEstateRepository(someEstateService->theEstateRepository);
    dynamicArray * repositoryRecordings = someEstateService->theRedoOperations->repositoryRecordings;
    someEstateService->theEstateRepository = repositoryRecordings->elements[repositoryRecordings->length - 1];
    deleteRedoOperation(someEstateService->theRedoOperations);
}
