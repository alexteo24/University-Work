//
// Created by Teo on 3/14/2021.
//

#include "TestsDynamicArray.h"
#include "DynamicArray.h"
#include <assert.h>
#include <stdio.h>
#include "../Domain/Domain.h"
#include <string.h>
void testDynamicArray() {
    printf("\nTesting dynamic array!\n");
    dynamicArray * newArray = createDynamicArray(10);
    assert(newArray->capacity == 10);
    assert(newArray->length == 0);
    addElement(newArray, createEstate("HOUSE", "ORADEA", 120, 97000));
    assert(newArray->length == 1);
    addElement(newArray, createEstate("PENTHOUSE", "BUCHAREST", 150, 145000));
    assert(newArray->length == 2);
    addElement(newArray, createEstate("APARTMENT", "TELEORMAN", 75, 65000));
    assert(newArray->length == 3);
    destroyEstate(getElement(newArray, 1));
    deleteElement(newArray, 1);
    assert(newArray->length == 2);
    destroyEstate(getElement(newArray, 0));
    updateElement(newArray, 0, createEstate("APARTMENT", "IASI", 65, 70000));
    Estate * firstEstate = getElement(newArray, 0);
    assert(strcmp(firstEstate->estateType, "APARTMENT") == 0 && strcmp(firstEstate->estateAddress, "IASI") == 0 && firstEstate->estateSurface == 65 && firstEstate->estatePrice == 70000);
    resizeArray(newArray);
    assert(newArray->length == 2);
    assert(newArray->capacity == 20);
    assert(arrayLength(newArray) == 2);
    assert(arrayCapacity(newArray) == 20);
    int index;
    for (index = 0; index < newArray->length; index++) {
        Estate * currentEstate = getElement(newArray, index);
        destroyEstate(currentEstate);
    }
    destroyDynamicArray(&newArray);
    printf("\nDone!\n");
}