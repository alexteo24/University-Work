//
// Created by Teo on 3/11/2021.
//
#include "Domain.h"
#include <stdlib.h>
#include <string.h>

Estate * createEstate(char* estateType, char* estateAddress, int estateSurface, int estatePrice) {
    Estate * newEstate = (Estate*)malloc(sizeof(Estate));
    newEstate->estateType = (char*)malloc(sizeof(char ) * strlen(estateType) + 1);
    strcpy(newEstate->estateType, estateType);
    newEstate->estateAddress = (char*)malloc(sizeof (char ) * strlen(estateAddress) + 1);
    strcpy(newEstate->estateAddress, estateAddress);
    newEstate->estateSurface = estateSurface;
    newEstate->estatePrice = estatePrice;
    return newEstate;
}

void destroyEstate(Estate * someEstate) {
    free(someEstate->estateType);
    free(someEstate->estateAddress);
    free(someEstate);
}

Estate * copyEstate(Estate * someEstate) {
    Estate * copyOfEstate = createEstate(someEstate->estateType, someEstate->estateAddress, someEstate->estateSurface, someEstate->estatePrice);
    return copyOfEstate;
}