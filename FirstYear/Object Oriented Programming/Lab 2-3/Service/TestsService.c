//
// Created by Teo on 3/14/2021.
//

#include "TestsService.h"
#include <stdio.h>
#include "../UndoRedo/UndoRedo.h"
#include <assert.h>
void testService() {
    printf("\nTesting service!\n");
    estateRepository * newRepository = createEstateRepository(10);
    initRepository(newRepository);
    estateService *newService = createEstateService(newRepository);
    Estate * newEstate = createEstate("APARTMENT", "GIURGIU", 90, 95000);
    bool status = addEstateService(newService, newEstate);
    assert(status == true);
    assert(newService->theEstateRepository->estatesList->length == 11);
    assert(newService->theEstateRepository->estatesList->capacity == 20);
    assert(newService->theUndoOperations->repositoryRecordings->length == 1);
    newEstate = createEstate("APARTMENTOS", "GIURGIU", 90, 95000);
    status = addEstateService(newService, newEstate);
    assert(status == false);
    assert(newService->theEstateRepository->estatesList->length == 11);
    assert(newService->theEstateRepository->estatesList->capacity == 20);
    assert(newService->theUndoOperations->repositoryRecordings->length == 1);
    status = removeEstateService(newService, "GIURGIU");
    assert(status == true);
    assert(newService->theEstateRepository->estatesList->length == 10);
    assert(newService->theEstateRepository->estatesList->capacity == 20);
    assert(newService->theUndoOperations->repositoryRecordings->length == 2);
    status = removeEstateService(newService, "GIURGIU");
    assert(status == false);
    assert(newService->theEstateRepository->estatesList->length == 10);
    assert(newService->theEstateRepository->estatesList->capacity == 20);
    assert(newService->theUndoOperations->repositoryRecordings->length == 2);
    Estate * updatedEstate = createEstate("APARTMENT", "ORADEA", 120, 97000);
    status = updateEstateService(newService, updatedEstate);
    assert(status == true);
    assert(newService->theUndoOperations->repositoryRecordings->length == 3);
    updatedEstate = createEstate("APARTMENT", "ODEA", 120, 97000);
    status = updateEstateService(newService, updatedEstate);
    assert(status == false);
    assert(newService->theUndoOperations->repositoryRecordings->length == 3);
    dynamicArray * matchingArray = findAllMatchingEstates(newService, "", "SURFACE");
    assert(matchingArray->length == newService->theEstateRepository->estatesList->length);
    destroyDynamicArray(&matchingArray);
    matchingArray = findAllMatchingEstates(newService, "xyz", "SURFACE");
    assert(matchingArray->length == 0);
    destroyDynamicArray(&matchingArray);
    matchingArray = findPriceEstates(newService, 100000, "ASCENDING");
    assert(matchingArray->length == 4);
    destroyDynamicArray(&matchingArray);
    matchingArray = findPriceEstates(newService, 200000, "ASCENDING");
    assert(matchingArray->length == 0);
    destroyDynamicArray(&matchingArray);
    matchingArray = findAllTypeEstates(newService, "HOUSE", 70, "ASCENDING");
    assert(matchingArray->length == 3);
    destroyDynamicArray(&matchingArray);
    matchingArray = findAllTypeEstates(newService, "PENTHOUSE", 70, "ASCENDING");
    assert(matchingArray->length == 2);
    destroyDynamicArray(&matchingArray);
    matchingArray = findAllTypeEstates(newService, "PENTHOUSE", 150, "ASCENDING");
    assert(matchingArray->length == 1);
    destroyDynamicArray(&matchingArray);
    undoSomeOperation(newService);
    assert(newService->theUndoOperations->repositoryRecordings->length == 2);
    assert(newService->theRedoOperations->repositoryRecordings->length == 1);
    undoSomeOperation(newService);
    assert(newService->theUndoOperations->repositoryRecordings->length == 1);
    assert(newService->theRedoOperations->repositoryRecordings->length == 2);
    redoSomeOperation(newService);
    assert(newService->theUndoOperations->repositoryRecordings->length == 2);
    assert(newService->theRedoOperations->repositoryRecordings->length == 1);
    redoSomeOperation(newService);
    assert(newService->theUndoOperations->repositoryRecordings->length == 3);
    assert(newService->theRedoOperations->repositoryRecordings->length == 0);
    destroyEstateService(newService);
    printf("\nDone!\n");
}