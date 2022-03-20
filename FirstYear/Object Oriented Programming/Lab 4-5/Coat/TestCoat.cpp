//
// Created by Teo on 3/26/2021.
//

#include "TestCoat.h"
#include <cassert>
#include <iostream>

void testCoat() {
    Coat newCoat("XL", "RED", 10, 100, "someshadylink", "asdfghj");
    Coat otherCoat(newCoat);
    assert(otherCoat.getSize() == "XL");
    assert(otherCoat.getColour() == "RED");
    assert(otherCoat.getPrice() == 10);
    assert(otherCoat.getQuantity() == 100);
    assert(otherCoat.getPhotographLink() == "someshadylink");
    assert(otherCoat.getUniqueID() == "asdfghj");
    assert(newCoat == otherCoat);
    otherCoat.setSize("XXL");
    otherCoat.setColor("SOMERED");
    otherCoat.setPrice(100);
    otherCoat.setQuantity(1000);
    otherCoat.setPhotographLink("anothershadylink");
    otherCoat.setUniqueID("qwertyu");
    assert(otherCoat.getSize() == "XXL");
    assert(otherCoat.getColour() == "SOMERED");
    assert(otherCoat.getPrice() == 100);
    assert(otherCoat.getQuantity() == 1000);
    assert(otherCoat.getPhotographLink() == "anothershadylink");
    assert(otherCoat.getUniqueID() == "qwertyu");
    assert(newCoat != otherCoat);
}