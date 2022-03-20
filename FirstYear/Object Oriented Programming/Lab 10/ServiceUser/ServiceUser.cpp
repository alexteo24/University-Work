//
// Created by Teo on 4/12/2021.
//

#include "ServiceUser.h"
#include <algorithm>
#include <iostream>

ServiceUser::ServiceUser(RepositoryCoatsFile &repositoryCoatsFile, RepositoryShopping *repositoryShopping) : _repositoryCoatsFile{repositoryCoatsFile},
                                                                                                            _repositoryShopping{repositoryShopping},
                                                                                                            _matchingCoats{_repositoryCoatsFile.getVector().size()} {
    findMatchingSize("");
}

void ServiceUser::findMatchingSize(const std::string &size) {
    std::vector<Coat> matchingCoats {_repositoryCoatsFile.getVector().size()};
    auto it = std::copy_if(_repositoryCoatsFile.getVector().begin(), _repositoryCoatsFile.getVector().end(),
                           matchingCoats.begin(), [size](const Coat &c) { return c.getSize() == size || size.length() == 0; });
    matchingCoats.resize(std::distance(matchingCoats.begin(), it));
    _matchingCoats = matchingCoats;
}

std::vector<Coat> ServiceUser::getCartForPrint() {
    return _repositoryShopping->getVector();
}

Coat& ServiceUser::nextItem() {
    if (_matchingCoats.size() - 1 - current > 0) {
        current++;
    }
    else {
        current = 0;
    }
    return _matchingCoats[current];
}

void ServiceUser::addToCart(Coat& coat, int amount) {
    Coat buyCoat = coat;
    if (amount > coat.getQuantity()) {
        throw ShoppingException("There are not enough coats left!\n");
    }
    auto anotherIt = find(_matchingCoats.begin(), _matchingCoats.end(), coat);
    auto it = find(_repositoryShopping->getVector().begin(), _repositoryShopping->getVector().end(), coat);
    if (it == _repositoryShopping->getVector().end()) {
        buyCoat.setQuantity(amount);
        std::unique_ptr<Operation> addOperation = std::make_unique<AddOperationUser>(_repositoryShopping, buyCoat);
        _undoVector.push_back(std::move(addOperation));
        _redoVector.clear();
        _repositoryShopping->addCoatRepo(buyCoat);
    } else {
        if (amount + it->getQuantity() <= coat.getQuantity()) {
            buyCoat.setQuantity(it->getQuantity() + amount);
            updateEntryFromCart(buyCoat, *it);
        } else {
            throw ShoppingException("There are not enough coats left!\n");
        }
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


std::vector<Coat>& ServiceUser::getCoatList() {
    return _repositoryCoatsFile.getVector();
}

std::vector<Coat>& ServiceUser::getMatchingList() {
    return _matchingCoats;
}

void ServiceUser::setRepo(const std::string& type) {
    if (type == "csv") {
        _repositoryShopping = std::make_unique<CSVShoppingBasket>().get();
    } else {
        _repositoryShopping = std::make_unique<HTMLShoppingBasket>().get();
    }
}

void ServiceUser::deleteFromCart(Coat &coat) {
    auto it = std::find(_repositoryShopping->getVector().begin(), _repositoryShopping->getVector().end(), coat);
    if (it != _repositoryShopping->getVector().end()) {
        std::unique_ptr<Operation> deleteOperation = std::make_unique<DeleteOperationUser>(_repositoryShopping, *it);
        _undoVector.push_back(std::move(deleteOperation));
        _redoVector.clear();
        _repositoryShopping->getVector().erase(it);
    }
}

void ServiceUser::updateEntryFromCart(Coat &newCoat, Coat &oldCoat) {
    if (newCoat.getQuantity() == 0) {
        deleteFromCart(oldCoat);
    } else {
        std::unique_ptr<Operation> updateOperation = std::make_unique<UpdateOperationUser>(_repositoryShopping, newCoat, oldCoat);
        _undoVector.push_back(std::move(updateOperation));
        _redoVector.clear();
        _repositoryShopping->updateCoatRepo(newCoat, oldCoat);
    }
}

void ServiceUser::undo() {
    if(_undoVector.empty()) {
        throw ShoppingException{"There is nothing to undo!"};
    }
    _undoVector.back()->undo();
    _redoVector.push_back(move(_undoVector.back()));
    _undoVector.pop_back();
}

void ServiceUser::redo() {
    if(_redoVector.empty()) {
        throw ShoppingException{"There is nothing to redo!"};
    }
    _redoVector.back()->redo();
    _undoVector.push_back(move(_redoVector.back()));
    _redoVector.pop_back();
}

ServiceUser::~ServiceUser() = default;
