//
// Created by Teo on 4/12/2021.
//

#ifndef REDONICE_SERVICEUSER_H
#define REDONICE_SERVICEUSER_H

#include "../RepositoryShopping/RepostioryShopping.h"
#include "../RepositoryCoats/RepositoryCoatsFile.h"
#include "ShoppingExceptions.h"

class ServiceUser {
private:
    RepositoryShopping* _repositoryShopping;
    RepositoryCoatsFile& _repositoryCoatsFile;
    int current = -1;

public:
    ServiceUser(RepositoryCoatsFile& repositoryCoatsFile, RepositoryShopping* repositoryShopping);

    std::vector<Coat> findMatchingSize(const std::string& size);

    ~ServiceUser();

    std::vector<Coat> getCartForPrint();

    Coat &nextItem(std::vector<Coat> &vector);

    void addToCart(Coat& coat, int amount, std::vector<Coat>& vector);

    int computeCost();

    void checkOut();

    void write();

    void open();
};

#endif //REDONICE_SERVICEUSER_H
