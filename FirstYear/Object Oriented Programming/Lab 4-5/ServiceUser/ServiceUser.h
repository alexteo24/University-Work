//
// Created by Teo on 3/24/2021.
//

#ifndef A45_ALEXTEO24_SERVICEUSER_H
#define A45_ALEXTEO24_SERVICEUSER_H
#include "../RepositoryShopping/RepositoryShopping.h"
#include "../RepositoryCoats/RepositoryCoats.h"

class ServiceUser {
private:
    RepositoryCoats& repositoryCoats;
    RepositoryShopping repositoryShopping;
    int current = -1;

public:

    /// Constructor
    /// \param repositoryShopping - repository for the buying
    /// \param repositoryCoats - repository with the coats
    ServiceUser(const RepositoryShopping& repositoryShopping, RepositoryCoats &repositoryCoats);

    /// Destructor
    ~ServiceUser();

    /// Adding a a coat to the shopping cart
    /// \param someCoat - the coat we want to add (buy)
    /// \param quantity - the quantity we want to add (buy)
    /// \param matchingSize - the list of the coats matching a certain size
    /// \return - Message regarding the status of the addition
    std::string addToCart(const Coat& someCoat, int quantity, dynamicArray<Coat> matchingSize);

    /// Getting the next item in the list
    /// \param matchingSize - the list of coats matching a certain size
    /// \return - the current coat
    Coat nextItem(dynamicArray<Coat> matchingSize);

    /// Getting a list of coats having a certain size
    /// \param size - the size we want to find
    /// \return - the list of the coats having a certain size
    dynamicArray<Coat> findMatchingSize(const std::string& size);

    dynamicArray<Coat> getCartForPrint();

    /// Computing the cost of all coats in the shopping cart
    /// \return - the cost
    int computeCost();

    /// Updating the stock left
    void checkOut();
};


#endif //A45_ALEXTEO24_SERVICEUSER_H
