//
// Created by Teo on 3/11/2021.
//

#include "Repository.h"
#include <stdlib.h>
#include <string.h>
estateRepository * createEstateRepository(int defaultCapacity)
/// This function is responsible for creating an instance for the estateRepository
/// \param defaultCapacity - the capacity of the dynamic array which will be created for the repository
/// \return - the address of the newly created repository
{
    estateRepository * newEstateRepository = (estateRepository*)malloc(sizeof (estateRepository));
    newEstateRepository->estatesList = createDynamicArray(defaultCapacity);
    return newEstateRepository;
}

estateRepository * copyEstateRepository(estateRepository * someEstateRepository)
/// This function is responsible for copying the estateRepository to a newly created instance
/// \param someEstateRepository - the estateRepository we want to copy
/// \return - the address of the copy of the estateRepository
{
    estateRepository * copyEstateRepository = (estateRepository*)malloc(sizeof (estateRepository));
    copyEstateRepository->estatesList = createDynamicArray(someEstateRepository->estatesList->capacity);
    int index;
    for(index = 0; index < someEstateRepository->estatesList->length; index++) {
        Estate * estateForCopy = getElement(someEstateRepository->estatesList, index);
        addElement(copyEstateRepository->estatesList, copyEstate(estateForCopy));
    }
    return copyEstateRepository;
}

void initRepository(estateRepository * someEstateRepository)
/// This function is responsible for adding 10 instances to the repository
/// \param someEstateRepository - the repository to which we want to add the estates
{
    addEstate(someEstateRepository, createEstate("HOUSE", "ORADEA", 120, 97000));
    addEstate(someEstateRepository, createEstate("PENTHOUSE", "BUCHAREST", 150, 145000));
    addEstate(someEstateRepository, createEstate("APARTMENT", "TELEORMAN", 75, 65000));
    addEstate(someEstateRepository, createEstate("APARTMENT", "CONSTANTA", 78, 80000));
    addEstate(someEstateRepository, createEstate("APARTMENT", "IASI", 65, 70000));
    addEstate(someEstateRepository, createEstate("HOUSE", "ARAD", 135, 120000));
    addEstate(someEstateRepository, createEstate("PENTHOUSE", "TIMISOARA", 175, 180000));
    addEstate(someEstateRepository, createEstate("HOUSE", "BRASOV", 105, 115000));
    addEstate(someEstateRepository, createEstate("HOUSE", "SIBIU", 95, 81000));
    addEstate(someEstateRepository, createEstate("APARTMENT", "CLUJ-NAPOCA", 60, 65000));
}

void destroyAllEstates(estateRepository * someEstateRepository)
/// This function is responsible for destroying all the Estate in someEstateRepository
/// \param someEstateRepository - the repository from which we want to destroy all the estates
{
    int nrEstates = someEstateRepository->estatesList->length;
    int index;
    for (index = 0; index < nrEstates; index++) {
        destroyEstate(someEstateRepository->estatesList->elements[index]);
    }
}

void destroyEstateRepository(estateRepository * someEstateRepository)
/// This function is responsible for destroying the repository
/// \param someEstateRepository - the repository we want to destroy
{
    destroyAllEstates(someEstateRepository);
    destroyDynamicArray(&someEstateRepository->estatesList);
    free(someEstateRepository);
}

void addEstate(estateRepository * someEstateRepository, Estate * newEstate)
/// This function is responsible for adding a new estate to the repository
/// \param someEstateRepository - the repository to which we want to add the new estate
/// \param newEstate - the new estate to be added
{
    addElement(someEstateRepository->estatesList, newEstate);
}

bool removeEstate(estateRepository * someEstateRepository, char* estateAddressRemoval)
/// This function is responsible for removing an estate from the repository, based on the address
/// \param someEstateRepository - the repository from which we want to remove the estate
/// \param estateAddressRemoval - the address of the estate we want to remove
/// \return - True if the estate we want to remove existed and was removed, false otherwise
{
    int elementPosition = findEstate(someEstateRepository, estateAddressRemoval);
    if (elementPosition == -1) {
        return false;
    }
    else
    {
        destroyEstate(someEstateRepository->estatesList->elements[elementPosition]);
        deleteElement(someEstateRepository->estatesList, elementPosition);
        return true;
    }
}

bool updateEstate(estateRepository * someEstateRepository, Estate * newEstate)
/// This function is responsible for updating an element, based on its address
/// \param someEstateRepository - the repository in which we want to update the estate having the same address as the newEstate
/// \param newEstate - the updated estate, its address should match one of the already existing estates
/// \return - True if there is an estate having the same address as the newEstate and the update is successful, false otherwise
{
    int elementPosition = findEstate(someEstateRepository, newEstate->estateAddress);
    if (elementPosition == -1) {
        destroyEstate(newEstate);
        return false;
    }
    else
    {
        destroyEstate(someEstateRepository->estatesList->elements[elementPosition]);
        updateElement(someEstateRepository->estatesList, elementPosition, newEstate);
        return true;
    }
}

int findEstate(estateRepository * someEstateRepository, char* estateAddressSearch)
/// This function is responsible for searching for an estate based on its address
/// \param someEstateRepository - the repository in which we want to find the estate
/// \param estateAddressSearch - the address of the estate we want to find
/// \return - the position of the estate in the array or -1 if the estate does not exist
{
    int nrEstates = someEstateRepository->estatesList->length;
    int index = 0;
    while (index < nrEstates) {
        Estate * searchEstate = getElement(someEstateRepository->estatesList, index);
        if (strcmp(searchEstate->estateAddress, estateAddressSearch) == 0) {
            return index;
        }
        index++;
    }
    return -1;
}