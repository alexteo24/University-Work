//
// Created by Teo on 3/26/2021.
//

#include "TestRepositoryShopping.h"
#include <cassert>

void testRepositoryShopping() {
    RepositoryShopping repositoryShopping;
    Coat newCoat("XL", "RED", 10, 100, "someshadylink", "asdfghj");
    assert(repositoryShopping.getDynamicArray().getLength() == 0);
    assert(repositoryShopping.findCoat(newCoat.getUniqueID()) == -1);
    repositoryShopping.addToShoppingCart(newCoat, 10);
    assert(repositoryShopping.getDynamicArray().getLength() == 1);
    assert(repositoryShopping.findCoat(newCoat.getUniqueID()) == 0);
    repositoryShopping.emptyCart();
    assert(repositoryShopping.getDynamicArray().getLength() == 0);
}