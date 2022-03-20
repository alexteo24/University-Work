//
// Created by Teo on 3/31/2021.
//
#pragma once
#ifndef REDONICE_SERVICEADMINISTRATOR_H
#define REDONICE_SERVICEADMINISTRATOR_H


#include <string>
#include "../RepositoryCoats/RepositoryCoats.h"
#include "../RepositoryCoats/RepositoryCoatsFile.h"
#include "../Validators/ValidatorCoat.h"

class ServiceAdministrator {
private:
    RepositoryCoatsFile& _repoCoats;

public:
    ServiceAdministrator(RepositoryCoatsFile& repoCoats);

    void addCoatService(const std::string& size, const std::string& color,const std::string& uniqueID,
                        const std::string& photographLink, int price, int quantity);

    void deleteCoatService(const std::string& sCoatID);

    void updateCoatService(const std::string& size, const std::string& color,const std::string& uniqueID,
                           const std::string& photographLink, int price, int quantity);

    std::vector<Coat>& getCoatList();
};


#endif //REDONICE_SERVICEADMINISTRATOR_H
