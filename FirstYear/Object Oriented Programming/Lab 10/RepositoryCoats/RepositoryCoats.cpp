//
// Created by Teo on 3/31/2021.
//

#include <iostream>
#include "RepositoryCoats.h"
#include <algorithm>
#include <iostream>

RepositoryCoats::RepositoryCoats() : _coatsStorage{}{}

RepositoryCoats::~RepositoryCoats() = default;

void RepositoryCoats::deleteCoatRepo(const std::string &sCoatID) {
    std::vector<Coat>::iterator it;
    it = std::find(_coatsStorage.begin(), _coatsStorage.end(), sCoatID);
    if (it == _coatsStorage.end()) {
        throw RepositoryCoatsException("There is no coat having this ID!\n");
    } else {
        if (it->getQuantity() != 0 ) {
            throw RepositoryCoatsException("The coat was not sold out!\n");
        } else {
            _coatsStorage.erase(it);
        }
    }
}

void RepositoryCoats::addCoatRepo(const Coat &sCoat) {
    std::vector<Coat>::iterator it;
    it = std::find(_coatsStorage.begin(), _coatsStorage.end(), sCoat);
    if (it != _coatsStorage.end()) {
        throw RepositoryCoatsException("There already exists a coat having this ID!\n");
    } else {
        _coatsStorage.push_back(sCoat);
    }
}

void RepositoryCoats::updateCoatRepo(const Coat &newCoat, const Coat &oldCoat) {
    std::vector<Coat>::iterator it;
    it = std::find(_coatsStorage.begin(), _coatsStorage.end(), oldCoat);
    if (it == _coatsStorage.end()) {
        throw RepositoryCoatsException("There is no coat having that ID!\n");
    } else {
        *it = newCoat;
    }
}

std::vector<Coat>& RepositoryCoats::getVector() {
    return _coatsStorage;
}

void RepositoryCoats::initRepo() {
    addCoatRepo(Coat("M", "IRIS", "LFKEJSG", "https://www.trenchiris.com", 135, 10));
    addCoatRepo(Coat("S", "PEA", "JDEAXMF", "https://www.trenchpea.com", 130, 7));
    addCoatRepo(Coat("L", "DARK BLUE", "ITNVSF", "https://www.trenchdblue.com", 95, 15));
    addCoatRepo(Coat("XL", "COBALT", "FJSNVUR", "https://www.trenchcobalt.com", 150, 12));
    addCoatRepo(Coat("M", "RED", "GKDNEBX", "https://www.trenchred.com", 160, 13));
    addCoatRepo(Coat("XXL", "BLACK", "ONGDSOI",  "https://www.trenchblack.com",190, 20));
    addCoatRepo(Coat("XL", "LEOPARD", "OBISGRC", "https://www.trenchleopard.com", 120, 30));
    addCoatRepo(Coat("M", "BUTTERCREAM", "PHSJIDG", "https://www.trenchbuttercream.com", 390, 9));
    addCoatRepo(Coat("S", "GRAY", "OGIHASQ", "https://www.trenchgray.com", 220, 11));
    addCoatRepo(Coat("XXXL", "CHESTNUT", "FEOIAHF", "https://www.trenchchestnut.com", 2000, 5));
}
