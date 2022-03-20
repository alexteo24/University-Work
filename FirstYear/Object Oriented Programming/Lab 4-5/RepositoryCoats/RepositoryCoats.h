//
// Created by Teo on 3/16/2021.
//

#ifndef A45_ALEXTEO24_REPOSITORYCOATS_H
#define A45_ALEXTEO24_REPOSITORYCOATS_H
#include "../DynamicArray/DynamicArray.h"
#include "../Coat/Coat.h"
#include <cstring>
class RepositoryCoats {
private:
    dynamicArray<Coat> coatsStorage;

public:
    /// Constructor
    /// \param capacity the initial capacity
    RepositoryCoats(int capacity);

    /// Destructor
    ~RepositoryCoats();

    /// Adding a new coat to the coats storage
    /// \param newCoat - the coat we want to add
    void addNewCoat(const Coat& newCoat);

    /// Removing a coat from the coats storage
    /// \param someCoat - the coat we want to remove
    void removeCoat(const Coat& someCoat);

    /// Updating a coat in the coats storage
    /// \param updatedCoat - the coat with the new data
    /// \param oldCoat - the coat with the old data
    void updateCoat(const Coat& updatedCoat, const Coat& oldCoat);

    /// Searching for a coat based on its unique id
    /// \param uniqueID - the unique id of the coat
    /// \return - the position in the array or -1 if it was not found
    int findCoat(const std::string& uniqueID);

    /// Getter for coats storage
    /// \return - the coats storage
    dynamicArray<Coat> getDynamicArray();

    /// Adding 10 default entries to the repostiory
    void initRepository();

};

#endif //A45_ALEXTEO24_REPOSITORYCOATS_H
