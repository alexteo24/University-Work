//
// Created by Teo on 3/11/2021.
//

#ifndef A23_ALEXTEO24_SERVICE_H
#define A23_ALEXTEO24_SERVICE_H
#include "../Repository/Repository.h"
#include "../UndoRedo/UndoRedo.h"
typedef struct {
    estateRepository * theEstateRepository;
    undoOperations * theUndoOperations;
    redoOperations * theRedoOperations;
}estateService;

estateService * createEstateService(estateRepository * someEstateRepository);

void destroyEstateService(estateService * someEstateService);

bool addEstateService(estateService * someEstateService, Estate * newEstate);

bool removeEstateService(estateService * someEstateService, char* estateAddress);

bool updateEstateService(estateService * someEstateService, Estate * updatedEstate);

dynamicArray * findAllMatchingEstates(estateService * someEstateService, char * estatePartialAddress, char *option);

dynamicArray * findAllTypeEstates(estateService * someEstateService, char *estateType, int estateSurface, char *option);

dynamicArray * findPriceEstates(estateService * someEstateService, int estatePrice, char * option);

void undoSomeOperation(estateService * someEstateService);

void redoSomeOperation(estateService * someEstateService);


#endif //A23_ALEXTEO24_SERVICE_H
