//
// Created by Teo on 3/14/2021.
//

#include "TestsRepository.h"
#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
void testRepository() {
    printf("\nTesting repository!\n");
    estateRepository * newRepository = createEstateRepository(10);
    initRepository(newRepository);
    assert(newRepository->estatesList->length == 10);
    assert(newRepository->estatesList->capacity == 10);
    addEstate(newRepository, createEstate("HOUSE", "GIURGIU", 90, 100000));
    assert(newRepository->estatesList->length == 11);
    assert(newRepository->estatesList->capacity == 20);
    bool status = removeEstate(newRepository, "GIURGIU");
    assert(status == true);
    assert(newRepository->estatesList->length == 10);
    assert(newRepository->estatesList->capacity == 20);
    status = removeEstate(newRepository, "BACAU");
    assert(status == false);
    Estate * updatedEstate = createEstate("APARTMENT", "ARAD", 90, 95000);
    status = updateEstate(newRepository, updatedEstate);
    assert(status == true);
    updatedEstate = createEstate("APARTMENT", "GIURGIUC", 90, 95000);
    status = updateEstate(newRepository, updatedEstate);
    assert(status == false);
    assert(findEstate(newRepository, "GIURGIUC") == -1);
    assert(findEstate(newRepository, "ORADEA") == 0);
    destroyEstateRepository(newRepository);
    printf("\nDone!\n");
}