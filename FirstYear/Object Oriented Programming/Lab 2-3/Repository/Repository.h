//
// Created by Teo on 3/11/2021.
//

#ifndef A23_ALEXTEO24_REPOSITORY_H
#define A23_ALEXTEO24_REPOSITORY_H
#include "../DynamicArray/DynamicArray.h"
#include <stdbool.h>
#include "../Domain/Domain.h"
typedef struct {
    dynamicArray * estatesList;
}estateRepository;

estateRepository * createEstateRepository(int defaultCapacity);

estateRepository * copyEstateRepository(estateRepository * someEstateRepository);

void initRepository(estateRepository * someEstateRepository);

void destroyAllEstates(estateRepository * someEstateRepository);

void destroyEstateRepository(estateRepository * someEstateRepository);

void addEstate(estateRepository * someEstateRepository, Estate * newEstate);

bool removeEstate(estateRepository * someEstateRepository, char* estateAddressRemoval);

bool updateEstate(estateRepository * someEstateRepository, Estate * newEstate);

int findEstate(estateRepository * someEstateRepository, char* estateAddressSearch);


#endif //A23_ALEXTEO24_REPOSITORY_H
