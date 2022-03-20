//
// Created by Teo on 3/14/2021.
//

#include "TestsDomain.h"
#include "Domain.h"
#include <assert.h>
#include <string.h>
#include <stdio.h>
void testDomain() {
    printf("\nTesting domain!\n");
    Estate * newEstate = createEstate("HOUSE", "CLUJ", 100, 125000);
    assert(newEstate->estatePrice == 125000);
    assert(newEstate->estateSurface == 100);
    assert(strcmp(newEstate->estateType, "HOUSE") == 0);
    assert(strcmp(newEstate->estateAddress, "CLUJ") == 0);
    Estate * otherEstate = copyEstate(newEstate);
    assert(otherEstate->estatePrice == newEstate->estatePrice);
    assert(otherEstate->estateSurface == newEstate->estateSurface);
    assert(strcmp(otherEstate->estateType, newEstate->estateType) == 0);
    assert(strcmp(otherEstate->estateAddress, newEstate->estateAddress) == 0);
    assert(newEstate != otherEstate);
    destroyEstate(newEstate);
    destroyEstate(otherEstate);
    printf("\nDone!\n");
}
