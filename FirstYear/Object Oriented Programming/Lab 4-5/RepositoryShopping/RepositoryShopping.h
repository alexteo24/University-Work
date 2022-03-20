//
// Created by Teo on 3/24/2021.
//

#ifndef A45_ALEXTEO24_REPOSITORYSHOPPING_H
#define A45_ALEXTEO24_REPOSITORYSHOPPING_H
#include "../DynamicArray/DynamicArray.h"
#include "../Coat/Coat.h"

class RepositoryShopping {
private:
    dynamicArray<Coat> shoppingCart;

public:

    /// Constructor
    RepositoryShopping();

    /// Destructor
    ~RepositoryShopping();

    /// Searching for a coat based on its unique id
    /// \param uniqueID - the unique id of the coat we want to find
    /// \return - the position of the coat in the array
    int findCoat(const std::string& uniqueID);

    /// Adding a coat to the shopping cart
    /// \param coat - the coat we want to add
    /// \param someQuantity - the quantity we want to buy
    void addToShoppingCart(const Coat& coat, int someQuantity);

    /// Updating a coat in the shopping cart
    /// \param updatedCoat - the coat with updated quantity
    /// \param oldCoat - the coat with the old quantity
    void updateEntry(const Coat& updatedCoat, const Coat& oldCoat);

    void emptyCart();

    dynamicArray<Coat> getDynamicArray();


};
#endif //A45_ALEXTEO24_REPOSITORYSHOPPING_H
