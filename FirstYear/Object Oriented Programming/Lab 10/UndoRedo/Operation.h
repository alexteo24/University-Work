//
// Created by Teo on 5/30/2021.
//

#ifndef A10_ALEXTEO24_OPERATION_H
#define A10_ALEXTEO24_OPERATION_H
#include "../RepositoryCoats/RepositoryCoats.h"
#include "../RepositoryShopping/RepostioryShopping.h"

class Operation {
public:
    virtual void undo() = 0;

    virtual void redo() = 0;

};

class AddOperation: public Operation {
private:
    RepositoryCoats& _repositoryCoats;
    Coat _coat;

public:
    AddOperation(RepositoryCoats& repositoryCoats, Coat sCoat);

    void undo() override;

    void redo() override;
};

class DeleteOperation: public Operation{
private:
    RepositoryCoats& _repositoryCoats;
    Coat _coat;

public:
    DeleteOperation(RepositoryCoats& repositoryCoats, Coat sCoat);

    void undo() override;

    void redo() override;
};

class UpdateOperation: public Operation {
private:
    RepositoryCoats& _repositoryCoats;
    Coat _coat;
    Coat _oldCoat;

public:
    UpdateOperation(RepositoryCoats& repositoryCoats, Coat newCoat, Coat oldCoat);

    void undo() override;

    void redo() override;
};

class AddOperationUser: public Operation {
private:
    RepositoryShopping* _repositoryShopping;
    Coat _coat;

public:
    AddOperationUser(RepositoryShopping* repositoryShopping, Coat sCoat);

    void undo() override;

    void redo() override;
};

class DeleteOperationUser: public Operation{
private:
    RepositoryShopping* _repositoryShopping;
    Coat _coat;

public:
    DeleteOperationUser(RepositoryShopping* repositoryShopping, Coat sCoat);

    void undo() override;

    void redo() override;
};

class UpdateOperationUser: public Operation {
private:
    RepositoryShopping* _repositoryShopping;
    Coat _coat;
    Coat _oldCoat;

public:
    UpdateOperationUser(RepositoryShopping* repositoryShopping, Coat newCoat, Coat oldCoat);

    void undo() override;

    void redo() override;
};


#endif //A10_ALEXTEO24_OPERATION_H
