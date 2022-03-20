//
// Created by Teo on 3/31/2021.
//
#pragma once
#ifndef REDONICE_REPOSITORYCOATS_H
#define REDONICE_REPOSITORYCOATS_H
#include <vector>
#include "../Domain/Coat.h"
#include "ExceptionsRepoCoats.h"

class RepositoryCoats {
private:
     std::vector<Coat> _coatsStorage;

public:
    RepositoryCoats();

    ~RepositoryCoats();

    virtual void addCoatRepo(const Coat& sCoat);

    virtual void deleteCoatRepo(const std::string &sCoatID);

    virtual void updateCoatRepo(const Coat &sCoat);

    virtual std::vector<Coat>& getVector();

    void initRepo();

};


#endif //REDONICE_REPOSITORYCOATS_H
