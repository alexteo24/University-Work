//
// Created by Teo on 3/26/2021.
//

#include "TestDynamicArray.h"
#include <cassert>
#include <exception>

void testDynamicArray() {
    dynamicArray<Coat> someArray(10);
    someArray.setLength(1);
    someArray.setLength(0);
    assert(someArray.getLength() == 0);
    Coat newCoat("XL", "RED", 10, 100, "someshadylink", "asdfghj");
    Coat otherCoat(newCoat);
    otherCoat.setUniqueID("qwertyu");
    someArray.addElement(newCoat);
    assert(someArray.getLength() == 1);
    dynamicArray<Coat> copyArray(someArray);
    assert(copyArray.getLength() == 1);
    someArray.addElement(otherCoat);
    assert(someArray.getLength() == 2);
    dynamicArray<Coat> anotherArray(10);
    someArray.addElement(newCoat);
    someArray.addElement(newCoat);
    someArray.addElement(newCoat);
    someArray.addElement(newCoat);
    someArray.addElement(newCoat);
    someArray.addElement(newCoat);
    someArray.addElement(newCoat);
    someArray.addElement(newCoat);
    someArray.addElement(newCoat);
    assert(someArray.getLength() == 11);
    anotherArray = someArray;
    anotherArray = anotherArray;
    assert(anotherArray.getLength() == 11);
    assert(anotherArray.findElement(newCoat) == 0);
    otherCoat.setSize("XXXL");
    anotherArray.updateElement(otherCoat, otherCoat);
    anotherArray.deleteElement(otherCoat);
    assert(anotherArray[0] == newCoat);
    try {
        anotherArray[-1];
    }
    catch (std::exception&) {
        assert(true);
    }
}