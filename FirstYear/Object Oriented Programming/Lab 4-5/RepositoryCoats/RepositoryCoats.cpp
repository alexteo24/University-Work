//
// Created by Teo on 3/16/2021.
//
#include "RepositoryCoats.h"

RepositoryCoats::RepositoryCoats(int capacity): coatsStorage(dynamicArray<Coat>(capacity)) {}

RepositoryCoats::~RepositoryCoats() = default;

void RepositoryCoats::addNewCoat(const Coat& newCoat) {
    this->coatsStorage.addElement(newCoat);
}

void RepositoryCoats::removeCoat(const Coat& someCoat) {
    this->coatsStorage.deleteElement(someCoat);
}

void RepositoryCoats::updateCoat(const Coat& updatedCoat, const Coat& oldCoat) {
    this->coatsStorage.updateElement(updatedCoat, oldCoat);
}

int RepositoryCoats::findCoat(const std::string& uniqueID) {
    int index;
    for (index = 0; index < this->coatsStorage.getLength(); index++) {
        Coat someCoat = coatsStorage[index];
        if (coatsStorage[index].getUniqueID() == uniqueID) {
            return index;
        }
    }
    return -1;
}

dynamicArray<Coat> RepositoryCoats::getDynamicArray() {
    return this->coatsStorage;
}

void RepositoryCoats::initRepository() {
    addNewCoat(Coat("M", "IRIS", 135, 10, "https://www.trenchiris.com", "LFKEJSG"));
    addNewCoat(Coat("S", "PEA", 130, 7, "https://www.trenchpea.com", "JDEAXMF"));
    addNewCoat(Coat("L", "DARK BLUE", 95, 15, "https://www.trenchdblue.com", "ITNVSF"));
    addNewCoat(Coat("XL", "COBALT", 150, 12, "https://www.trenchcobalt.com", "FJSNVUR"));
    addNewCoat(Coat("M", "RED", 160, 13, "https://www.trenchred.com", "GKDNEBX"));
    addNewCoat(Coat("XXL", "BLACK", 190, 20, "https://www.trenchblack.com","ONGDSOI"));
    addNewCoat(Coat("XL", "LEOPARD", 120, 30, "https://www.trenchleopard.com", "OBISGRC"));
    addNewCoat(Coat("M", "BUTTERCREAM", 390, 9, "https://www.trenchbuttercream.com", "PHSJIDG"));
    addNewCoat(Coat("S", "GRAY", 220, 11, "https://www.trenchgray.com", "OGIHASQ"));
    addNewCoat(Coat("XXXL", "CHESTNUT", 2000, 5, "https://www.trenchchestnut.com", "FEOIAHF"));
}
