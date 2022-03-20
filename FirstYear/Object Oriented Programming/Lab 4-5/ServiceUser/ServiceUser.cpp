//
// Created by Teo on 3/24/2021.
//

#include "ServiceUser.h"

ServiceUser::ServiceUser(const RepositoryShopping &repositoryShopping, RepositoryCoats& repositoryCoats): repositoryCoats(repositoryCoats), repositoryShopping(repositoryShopping) {}

ServiceUser::~ServiceUser() = default;

std::string ServiceUser::addToCart(const Coat& someCoat, int quantity, dynamicArray<Coat> matchingSize) {
    int onPosition = repositoryShopping.findCoat(someCoat.getUniqueID());
    if (onPosition == -1) {
        int somePosition = repositoryCoats.findCoat(someCoat.getUniqueID());
        if (repositoryCoats.getDynamicArray()[somePosition].getQuantity() >= quantity) {
            repositoryShopping.addToShoppingCart(someCoat, quantity);
        } else {
            return "There are not enough coats left!!!";
        }
    }
    else {
        int currentQuantity = repositoryShopping.getDynamicArray()[onPosition].getQuantity();
        int storeDataPosition = matchingSize.findElement(someCoat);
        if (currentQuantity + quantity <= repositoryCoats.getDynamicArray()[storeDataPosition].getQuantity()) {
            Coat updatedCoat = repositoryShopping.getDynamicArray()[onPosition];
            updatedCoat.setQuantity(currentQuantity + quantity);
            repositoryShopping.updateEntry(updatedCoat, updatedCoat);
        }
        else {
            return "There are not enough coats left!!!";
        }
    }
    return "Item added to the cart!!!";
}

Coat ServiceUser::nextItem(dynamicArray<Coat> matchingSize) {
    if (current < matchingSize.getLength() - 1) {
        current++;
    }
    else {
        current = 0;
    }
    return matchingSize[current];
}

dynamicArray<Coat> ServiceUser::findMatchingSize(const std::string& size) {
    if (size.length() == 0) {
        dynamicArray<Coat> matchingList = repositoryCoats.getDynamicArray();
        return matchingList;
    }
    else
    {
        dynamicArray<Coat> matchingList(10);
        int index;
        for (index = 0; index < repositoryCoats.getDynamicArray().getLength(); index++) {
            if (repositoryCoats.getDynamicArray()[index].getSize() == size) {
                matchingList.addElement(repositoryCoats.getDynamicArray()[index]);
            }
        }
        return matchingList;
    }

}

int ServiceUser::computeCost() {
    int cost = 0;
    int index;
    for (index = 0; index < repositoryShopping.getDynamicArray().getLength(); index++) {
        cost += repositoryShopping.getDynamicArray()[index].getQuantity() * repositoryShopping.getDynamicArray()[index].getPrice();
    }
    return cost;
}

dynamicArray<Coat> ServiceUser::getCartForPrint() {
    return repositoryShopping.getDynamicArray();
}

void ServiceUser::checkOut() {
    int index;
    for (index = 0; index < repositoryShopping.getDynamicArray().getLength(); index++) {
        int shopPosition = repositoryCoats.findCoat(repositoryShopping.getDynamicArray()[index].getUniqueID());
        Coat shopCoat = repositoryCoats.getDynamicArray()[shopPosition]; // having stock
        int quantityLeft = shopCoat.getQuantity() - repositoryShopping.getDynamicArray()[index].getQuantity();
        shopCoat.setQuantity(quantityLeft);
        repositoryCoats.updateCoat(shopCoat, shopCoat);
    }
    this->current = -1;
    repositoryShopping.emptyCart();
}


