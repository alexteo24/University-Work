
//
// Created by Teo on 5/30/2021.
//

#include <algorithm>
#include "Operation.h"

AddOperation::AddOperation(RepositoryCoats &repositoryCoats, Coat sCoat): _repositoryCoats{repositoryCoats}, _coat{sCoat} {}

void AddOperation::undo() {
    auto it = std::find(_repositoryCoats.getVector().begin(), _repositoryCoats.getVector().end(), _coat);
    it->setQuantity(0);
    _repositoryCoats.deleteCoatRepo(_coat.getUniqueID());
}

void AddOperation::redo() {
    _repositoryCoats.addCoatRepo(_coat);
}

DeleteOperation::DeleteOperation(RepositoryCoats &repositoryCoats, Coat sCoat): _repositoryCoats{repositoryCoats}, _coat{sCoat} {}

void DeleteOperation::undo() {
    auto it = std::find(_repositoryCoats.getVector().begin(), _repositoryCoats.getVector().end(), _coat);
    it->setQuantity(0);
    _repositoryCoats.addCoatRepo(_coat);
}

void DeleteOperation::redo() {
    _repositoryCoats.deleteCoatRepo(_coat.getUniqueID());
}

UpdateOperation::UpdateOperation(RepositoryCoats &repositoryCoats, Coat newCoat, Coat oldCoat):
_repositoryCoats{repositoryCoats}, _coat{newCoat}, _oldCoat{oldCoat} {}

void UpdateOperation::undo() {
    _repositoryCoats.updateCoatRepo(_oldCoat, _coat);
}

void UpdateOperation::redo() {
    _repositoryCoats.updateCoatRepo(_coat, _oldCoat);
}

AddOperationUser::AddOperationUser(RepositoryShopping* repositoryShopping, Coat sCoat): _repositoryShopping{repositoryShopping},
_coat{sCoat} {}

void AddOperationUser::undo() {
    auto it = std::find(_repositoryShopping->getVector().begin(), _repositoryShopping->getVector().end(), _coat);
    it->setQuantity(0);
    _repositoryShopping->deleteCoatRepo(_coat.getUniqueID());
}

void AddOperationUser::redo() {
    _repositoryShopping->addCoatRepo(_coat);
}

DeleteOperationUser::DeleteOperationUser(RepositoryShopping* repositoryShopping, Coat sCoat): _repositoryShopping{repositoryShopping},
_coat{sCoat} {}

void DeleteOperationUser::undo() {
    _repositoryShopping->addCoatRepo(_coat);
}

void DeleteOperationUser::redo() {
    auto it = std::find(_repositoryShopping->getVector().begin(), _repositoryShopping->getVector().end(), _coat);
    it->setQuantity(0);
    _repositoryShopping->deleteCoatRepo(_coat.getUniqueID());
}

UpdateOperationUser::UpdateOperationUser(RepositoryShopping* repositoryShopping, Coat newCoat, Coat oldCoat):
        _repositoryShopping{repositoryShopping}, _coat{newCoat}, _oldCoat{oldCoat} {}

void UpdateOperationUser::undo() {
    _repositoryShopping->updateCoatRepo(_oldCoat, _coat);
}

void UpdateOperationUser::redo() {
    _repositoryShopping->updateCoatRepo(_coat, _oldCoat);
}
