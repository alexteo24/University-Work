//
// Created by Teo on 4/12/2021.
//

#ifndef REDONICE_REPOSTIORYSHOPPING_H
#define REDONICE_REPOSTIORYSHOPPING_H
#include <vector>
#include "../Domain/Coat.h"
#include "../RepositoryCoats/RepositoryCoats.h"

class RepositoryShopping : public RepositoryCoats{
public:
    RepositoryShopping();

    virtual ~RepositoryShopping();

    virtual void write()=0;

    virtual void open()=0;
};

class HTMLShoppingBasket : public RepositoryShopping {
public:
    HTMLShoppingBasket();

    void write() override;

    void open() override;

    ~HTMLShoppingBasket() override = default;
};

class CSVShoppingBasket : public RepositoryShopping {
public:
    CSVShoppingBasket();

    void write() override;

    void open() override;

    ~CSVShoppingBasket() override = default;
};

#endif //REDONICE_REPOSTIORYSHOPPING_H
