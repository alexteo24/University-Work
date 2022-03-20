//
// Created by Teo on 3/26/2021.
//

#include "TestRepositoryCoats.h"
#include <cassert>

void testRepositoryCoats() {
    RepositoryCoats repositoryCoats(10);
    repositoryCoats.initRepository();
    Coat newCoat("XL", "RED", 10, 100, "someshadylink", "asdfghj");
    Coat otherCoat(newCoat);
    otherCoat.setUniqueID("qwertyu");
    assert(repositoryCoats.getDynamicArray().getLength() == 10);
    repositoryCoats.addNewCoat(newCoat);
    assert(repositoryCoats.getDynamicArray().getLength() == 11);
    repositoryCoats.addNewCoat(otherCoat);
    assert(repositoryCoats.getDynamicArray().getLength() == 12);
    assert(repositoryCoats.findCoat("qwertyu") == 11);
    assert(repositoryCoats.findCoat("1234567") == -1);
    repositoryCoats.removeCoat(otherCoat);
    assert(repositoryCoats.getDynamicArray().getLength() == 11);
    repositoryCoats.updateCoat(otherCoat, newCoat);
}