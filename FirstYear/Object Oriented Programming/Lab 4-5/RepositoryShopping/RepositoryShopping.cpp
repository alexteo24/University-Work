//
// Created by Teo on 3/24/2021.
//

#include "RepositoryShopping.h"

RepositoryShopping::RepositoryShopping(): shoppingCart(10){}

RepositoryShopping::~RepositoryShopping() = default;

void RepositoryShopping::addToShoppingCart(const Coat &coat, int someQuantity) {
    Coat coatToAdd = coat;
    coatToAdd.setQuantity(someQuantity);
    shoppingCart.addElement(coatToAdd);
}

int RepositoryShopping::findCoat(const std::string& uniqueID) {
    int index;
    for (index = 0; index < this->shoppingCart.getLength(); index++) {
        Coat someCoat = shoppingCart[index];
        if (shoppingCart[index].getUniqueID() == uniqueID) {
            return index;
        }
    }
    return -1;
}

dynamicArray<Coat> RepositoryShopping::getDynamicArray() {
    return shoppingCart;
}

void RepositoryShopping::updateEntry(const Coat &updatedCoat, const Coat &oldCoat) {
    int foundOnPosition = findCoat(updatedCoat.getUniqueID());
    if (foundOnPosition != -1) {
        shoppingCart.updateElement(updatedCoat, oldCoat);
    }
}

void RepositoryShopping::emptyCart() {
    shoppingCart.setLength(0);
}
