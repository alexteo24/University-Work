//
// Created by Teo on 3/17/2021.
//
#include "ServiceAdmin.h"

ServiceAdministrator::ServiceAdministrator(RepositoryCoats& repositoryCoats): repositoryCoats(repositoryCoats) {}

ServiceAdministrator::~ServiceAdministrator() = default;

bool ServiceAdministrator::addNewCoatService(const Coat& newCoat) {
    int foundOnPosition = this->repositoryCoats.findCoat(newCoat.getUniqueID());
    if (foundOnPosition == -1) {
        this->repositoryCoats.addNewCoat(newCoat);
        return true;
    }
    return false;
}

bool ServiceAdministrator::deleteCoatService(const std::string& uniqueID) {
    int deletePosition = this->repositoryCoats.findCoat(uniqueID);
    if (deletePosition != -1) {
        Coat toDeleteCoat = repositoryCoats.getDynamicArray()[deletePosition];
        if (toDeleteCoat.getQuantity() == 0) {
            this->repositoryCoats.removeCoat(this->repositoryCoats.getDynamicArray()[deletePosition]);
            return true;
        }
        else {
            return false;
        }
    }
    return false;
}

bool ServiceAdministrator::updateCoatService(const Coat& updatedCoat) {
    int updatePosition = this->repositoryCoats.findCoat(updatedCoat.getUniqueID());
    if (updatePosition != -1) {
        this->repositoryCoats.updateCoat(updatedCoat, repositoryCoats.getDynamicArray()[updatePosition]);
        return true;
    }
    return false;
}

RepositoryCoats ServiceAdministrator::getRepository() {
    return this->repositoryCoats;
}


