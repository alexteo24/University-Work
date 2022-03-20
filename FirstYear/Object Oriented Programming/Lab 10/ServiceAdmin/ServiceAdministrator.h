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
#include "../UndoRedo/Operation.h"

class ServiceAdministrator {
private:
    RepositoryCoatsFile& _repoCoats;
    std::vector<std::unique_ptr<Operation>> _undoVector;
    std::vector<std::unique_ptr<Operation>> _redoVector;

public:
    ServiceAdministrator(RepositoryCoatsFile& repoCoats);

    void addCoatService(const std::string& size, const std::string& color,const std::string& uniqueID,
                        const std::string& photographLink, int price, int quantity);

    void deleteCoatService(const std::string& sCoatID);

    void updateCoatService(const std::string& size, const std::string& color,const std::string& uniqueID,
                           const std::string& photographLink, int price, int quantity);

    std::vector<Coat>& getCoatList();

    int amountOnSize(const std::string& size);

    RepositoryCoatsFile& getRepository();

    void undo();

    void redo();
};


#endif //REDONICE_SERVICEADMINISTRATOR_H
