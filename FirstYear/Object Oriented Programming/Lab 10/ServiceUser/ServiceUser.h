//
// Created by Teo on 4/12/2021.
//

#ifndef REDONICE_SERVICEUSER_H
#define REDONICE_SERVICEUSER_H

#include "../RepositoryShopping/RepostioryShopping.h"
#include "../RepositoryCoats/RepositoryCoatsFile.h"
#include "../UndoRedo/Operation.h"
#include "ShoppingExceptions.h"
#include <memory>

class ServiceUser {
private:
    RepositoryShopping* _repositoryShopping;
    RepositoryCoatsFile& _repositoryCoatsFile;
    std::vector<Coat> _matchingCoats;
    std::vector<std::unique_ptr<Operation>> _undoVector;
    std::vector<std::unique_ptr<Operation>> _redoVector;
    int current = -1;

public:
    ServiceUser(RepositoryCoatsFile& repositoryCoatsFile, RepositoryShopping* repositoryShopping);

    void findMatchingSize(const std::string& size);

    ~ServiceUser();

    std::vector<Coat> getCartForPrint();

    Coat& nextItem();

    bool anyMatchingCoats() {return _matchingCoats.empty();}

    void addToCart(Coat& coat, int amount);

    int computeCost();

    void checkOut();

    std::vector<Coat>& getCoatList();

    std::vector<Coat>& getMatchingList();

    void setRepo(const std::string& type);

    void deleteFromCart(Coat& coat);

    void updateEntryFromCart(Coat& newCoat, Coat& oldCoat);

    void undo();

    void redo();

    void write();

    void open();
};

#endif //REDONICE_SERVICEUSER_H
