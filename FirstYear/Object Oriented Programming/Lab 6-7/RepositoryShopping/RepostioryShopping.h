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

    ~RepositoryShopping();

    virtual void write()=0;

    virtual void open()=0;
};

class HTMLAdoptionList : public RepositoryShopping {
public:
    HTMLAdoptionList();

    void write() override;

    void open() override;

    ~HTMLAdoptionList() = default;
};

class CSVAdoptionList : public RepositoryShopping {
public:
    CSVAdoptionList();

    void write() override;

    void open() override;

    ~CSVAdoptionList() = default;
};

#endif //REDONICE_REPOSTIORYSHOPPING_H
