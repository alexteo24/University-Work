//
// Created by Teo on 3/26/2021.
//

#include "ServiceUser.h"
#include <cassert>
#include <iostream>

void testServiceUser() {
    RepositoryCoats repositoryCoats(10);
    repositoryCoats.initRepository();
    RepositoryShopping repositoryShopping;
    ServiceUser serviceUser(repositoryShopping, repositoryCoats);
    Coat newCoat ("M", "IRIS", 135, 10, "https://www.trenchiris.com", "LFKEJSG");
    dynamicArray<Coat> matching = serviceUser.findMatchingSize("M");
    assert(matching.getLength() == 3);
    assert(serviceUser.addToCart(newCoat, 5, matching) == "Item added to the cart!!!");
    assert(serviceUser.addToCart(newCoat, 4, matching) == "Item added to the cart!!!");
    assert(serviceUser.addToCart(newCoat, 2, matching) == "There are not enough coats left!!!");
    Coat someCoat = serviceUser.nextItem(matching);
    assert(someCoat.getUniqueID() == "LFKEJSG");
    dynamicArray<Coat> other = serviceUser.findMatchingSize("");
    assert(other.getLength() == 10);
    dynamicArray<Coat> print = serviceUser.getCartForPrint();
    assert(print.getLength() == 1);
    someCoat = serviceUser.nextItem(matching);
    someCoat = serviceUser.nextItem(matching);
    someCoat = serviceUser.nextItem(matching);
    assert(serviceUser.computeCost() == 1215);
    serviceUser.checkOut();
    assert(repositoryCoats.getDynamicArray()[0].getQuantity() == 1);
}