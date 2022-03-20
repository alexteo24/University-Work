//
// Created by Teo on 4/11/2021.
//
#pragma once
#ifndef REDONICE_REPOSITORYCOATSFILE_H
#define REDONICE_REPOSITORYCOATSFILE_H
#include "RepositoryCoats.h"
#include "../Validators/ValidatorCoat.h"

class RepositoryCoatsFile : public RepositoryCoats
{
public:
    RepositoryCoatsFile();

    ~RepositoryCoatsFile();

    void addCoatRepo(const Coat &sCoat) override;

    void deleteCoatRepo(const std::string& sCoatID) override;

    void updateCoatRepo(const Coat &newCoat, const Coat& oldCoat) override;

    std::vector<Coat>& getVector();

private:
    void readDataFromFile(const std::string &fileName);

    void writeDataToFile(const std::string &fileName);

//    std::vector<Coat>
};

#endif //REDONICE_REPOSITORYCOATSFILE_H
