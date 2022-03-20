//
// Created by Teo on 4/12/2021.
//

#include "ServiceUser.h"
#include <algorithm>
#include <iostream>

ServiceUser::ServiceUser(RepositoryCoatsFile &repositoryCoatsFile, RepositoryShopping *repositoryShopping) : _repositoryCoatsFile{repositoryCoatsFile},
                                                                                                            _repositoryShopping{repositoryShopping} {}

std::vector<Coat> ServiceUser::findMatchingSize(const std::string &size) {
    std::vector<Coat> matching(_repositoryCoatsFile.getVector().size());
    auto it = std::copy_if(_repositoryCoatsFile.getVector().begin(), _repositoryCoatsFile.getVector().end(),
                           matching.begin(), [size](const Coat& c) {return c.getSize() == size;});
    matching.resize(std::distance(matching.begin(), it));
    return matching;
}

std::vector<Coat> ServiceUser::getCartForPrint() {
    return _repositoryShopping->getVector();
}

Coat& ServiceUser::nextItem(std::vector<Coat>& vector) {
    if (vector.size() - 1 - current > 0) {
        current++;
    }
    else {
        current = 0;
    }
    return vector[current];
}

void ServiceUser::addToCart(Coat& coat, int amount, std::vector<Coat>& vector) {
    Coat buyCoat = coat;
    if (amount > coat.getQuantity()) {
        throw ShoppingException("There are not enough coats left!\n");
    }
    auto anotherIt = find(vector.begin(), vector.end(), coat);
    auto it = find(_repositoryShopping->getVector().begin(), _repositoryShopping->getVector().end(), coat);
    if (it == _repositoryShopping->getVector().end()) {
        buyCoat.setQuantity(amount);
        coat.setQuantity(coat.getQuantity() - amount);
        *anotherIt = coat;
        _repositoryShopping->addCoatRepo(buyCoat);
    } else {
        it->setQuantity(it->getQuantity() + amount);
        coat.setQuantity(coat.getQuantity() - amount);
        *anotherIt = coat;
        _repositoryShopping->addCoatRepo(buyCoat);
    }
}

int ServiceUser::computeCost() {
    int totalCost = 0;
    for (const Coat& c : _repositoryShopping->getVector()) {
        totalCost += c.getQuantity() * c.getPrice();
    }
    return totalCost;
}

void ServiceUser::checkOut() {
    for (const Coat& c : _repositoryShopping->getVector()) {
        auto it = find(_repositoryCoatsFile.getVector().begin(), _repositoryCoatsFile.getVector().end(), c);
        it->setQuantity(it->getQuantity() - c.getQuantity());
    }
    _repositoryShopping->getVector().clear();
}

void ServiceUser::write() {
    _repositoryShopping->write();
}

void ServiceUser::open() {
    _repositoryShopping->open();
}


ServiceUser::~ServiceUser() = default;
