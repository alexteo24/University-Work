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
}

void ServiceAdministrator::deleteCoatService(const std::string &sCoatID) {
    _repoCoats.deleteCoatRepo(sCoatID);
}

void
ServiceAdministrator::updateCoatService(const std::string &size, const std::string &color, const std::string &uniqueID,
                                        const std::string &photographLink, int price, int quantity) {
    ValidatorCoat::validateCoat(size, color, uniqueID, photographLink, price, quantity);
    Coat sCoat{size, color, uniqueID, photographLink, price, quantity};
    _repoCoats.updateCoatRepo(sCoat);
}

std::vector<Coat>& ServiceAdministrator::getCoatList() {
    return _repoCoats.getVector();
}