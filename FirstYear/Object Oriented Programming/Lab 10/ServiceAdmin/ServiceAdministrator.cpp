//
// Created by Teo on 3/31/2021.
//

#include <iostream>
#include "ServiceAdministrator.h"

ServiceAdministrator::ServiceAdministrator(RepositoryCoatsFile& repoCoats):_repoCoats(repoCoats) {}

void ServiceAdministrator::addCoatService(const std::string &size, const std::string &color,
                                          const std::string &uniqueID,const std::string &photographLink,
                                          int price, int quantity) {
    ValidatorCoat::validateCoat(size, color, uniqueID, photographLink, price, quantity);
    Coat sCoat{size, color, uniqueID, photographLink, price, quantity};
    _repoCoats.addCoatRepo(sCoat);
    std::unique_ptr<Operation> addOperation = std::make_unique<AddOperation>(_repoCoats, sCoat);
    _undoVector.push_back(std::move(addOperation));
    _redoVector.clear();
}

void ServiceAdministrator::deleteCoatService(const std::string &sCoatID) {
    auto it = std::find(_repoCoats.getVector().begin(), _repoCoats.getVector().end(), sCoatID);
    if (it != _repoCoats.getVector().end()) {
        Coat oldCoat = *it;
        std::unique_ptr<Operation> deleteOperation = std::make_unique<DeleteOperation>(_repoCoats, oldCoat);
        _undoVector.push_back(std::move(deleteOperation));
        _redoVector.clear();
    }
    _repoCoats.deleteCoatRepo(sCoatID);

}

void
ServiceAdministrator::updateCoatService(const std::string &size, const std::string &color, const std::string &uniqueID,
                                        const std::string &photographLink, int price, int quantity) {
    ValidatorCoat::validateCoat(size, color, uniqueID, photographLink, price, quantity);
    Coat sCoat{size, color, uniqueID, photographLink, price, quantity};
    auto it = std::find(_repoCoats.getVector().begin(), _repoCoats.getVector().end(), uniqueID);
    Coat oldCoat{};
    if (it != _repoCoats.getVector().end()) {
        oldCoat = *it;
        std::unique_ptr<Operation> updateOperation = std::make_unique<UpdateOperation>(_repoCoats, sCoat, oldCoat);
        _undoVector.push_back(std::move(updateOperation));
        _redoVector.clear();
    }
    _repoCoats.updateCoatRepo(sCoat, oldCoat);
}

std::vector<Coat>& ServiceAdministrator::getCoatList() {
    return _repoCoats.getVector();
}

int ServiceAdministrator::amountOnSize(const std::string& size) {
    int amount = 0;
    for(Coat& sCoat:_repoCoats.getVector()) {
        if (sCoat.getSize() == size) {
            amount += sCoat.getQuantity();
        }
    }
    return amount;
}

RepositoryCoatsFile &ServiceAdministrator::getRepository() {
    return _repoCoats;
}

void ServiceAdministrator::undo() {
    if(_undoVector.empty()) {
        throw RepositoryCoatsException{"There is nothing to undo!"};
    }
    _undoVector.back()->undo();
    _redoVector.push_back(move(_undoVector.back()));
    _undoVector.pop_back();
}

void ServiceAdministrator::redo() {
    if(_redoVector.empty()) {
        throw RepositoryCoatsException{"There is nothing to redo!"};
    }
    _redoVector.back()->redo();
    _undoVector.push_back(move(_redoVector.back()));
    _redoVector.pop_back();
}
