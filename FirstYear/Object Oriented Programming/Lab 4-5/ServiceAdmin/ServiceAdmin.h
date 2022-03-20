//
// Created by Teo on 3/17/2021.
//
#pragma once
#ifndef A45_ALEXTEO24_SERVICEADMIN_H
#define A45_ALEXTEO24_SERVICEADMIN_H

#include "../RepositoryCoats/RepositoryCoats.h"

class ServiceAdministrator {
private:
    RepositoryCoats& repositoryCoats;

public:

    /// Constructor
    /// \param repositoryCoats - repo with al the coats
    ServiceAdministrator(RepositoryCoats& repositoryCoats);

    /// Destructor
    ~ServiceAdministrator();

    /// Adding a new coat to the repo
    /// \param newCoat - the coat we want to add
    /// \return - true if the addition was successful or false otherwise
    bool addNewCoatService(const Coat& newCoat);

    /// Deleting a coat from the repo
    /// \param uniqueID - the unique id of the coat we want to delete
    /// \return - true if the deletion was successful or false otherwise
    bool deleteCoatService(const std::string& uniqueID);

    /// Updating a coat in the repo
    /// \param updatedCoat - the coat with updated data (unique ID stays the same)
    /// \return - true if the update was successful or false otherwise
    bool updateCoatService(const Coat& updatedCoat);

    RepositoryCoats getRepository();



};
#endif //A45_ALEXTEO24_SERVICEADMIN_H
