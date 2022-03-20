//
// Created by Teo on 3/16/2021.
//

#ifndef A45_ALEXTEO24_COAT_H
#define A45_ALEXTEO24_COAT_H
#include <string>
class Coat {
private:
    std::string size;
    std::string color;
    int price;
    int quantity;
    std::string photographLink;
    std::string uniqueID;

public:

    /// Constructing the coat entity
    /// \param size - the size of the coat
    /// \param color - the color of the coat
    /// \param price - the price of the coat
    /// \param quantity - the quantity of the coat
    /// \param photographLink - the link to the photography of the coat
    /// \param uniqueID - the ID of the coat
    Coat(const std::string &size="", const std::string &color="", int price=0, int quantity=0,
         const std::string &photographLink="", const std::string &uniqueID="");

    /// Copy constructor
    /// \param otherCoat - the other coat
    Coat(const Coat &otherCoat);

    /// Setter for the size of the coat
    /// \param size - the size
    void setSize(const std::string &size);

    /// Setter for the color of the coat
    /// \param color - the color
    void setColor(const std::string &color);

    /// Setter fot the price of the coat
    /// \param price - the price
    void setPrice(int price);

    /// Setter for the quantity of the coat
    /// \param quantity - the quantity of the coat
    void setQuantity(int quantity);

    /// Setter for the photograph link of the coat
    /// \param photographLink - the link to the photograph
    void setPhotographLink(const std::string &photographLink);

    /// Setter for the unique id of the coat
    /// \param uniqueID - the unique id
    void setUniqueID(const std::string &uniqueID);

    /// Getter for the size of the coat
    /// \return - the size of the coat
    std::string getSize() const;

    /// Getter for the color of the coat
    /// \return - the color of the coat
    std::string getColour() const;

    /// Getter for the price of the coat
    /// \return - the price of the coat
    int getPrice();

    /// Getter for the quantity of the coat
    /// \return - the quantity of the coat
    int getQuantity();

    /// Getter for the photograph link of the coat
    /// \return - the photograph link of the coat
    std::string getPhotographLink() const;

    /// Getter for the unique id of the coat
    /// \return - the unique id of the coat
    std::string getUniqueID() const;

    /// Operator overloads
    Coat & operator=(const Coat &otherCoat);

    bool operator==(const Coat &otherCoat);

    bool operator!=(const Coat &otherCoat);

    friend std::ostream& operator<<(std::ostream& outStream, const Coat& coat);
};

#endif //A45_ALEXTEO24_COAT_H
