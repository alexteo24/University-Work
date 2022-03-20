//
// Created by Teo on 3/31/2021.
//
#pragma once
#ifndef REDONICE_COAT_H
#define REDONICE_COAT_H
#include <string>

class Coat {
private:
    std::string _size;
    std::string _color;
    std::string _uniqueID;
    std::string _photographLink;
    int _price;
    int _quantity;

public:
    Coat();
    Coat(const std::string& size, const std::string& color, const std::string& uniqueID,
         const std::string& photographLink, int price, int quantity);

    Coat(const Coat& otherCoat);
    std::string getSize() const;

    std::string getColor() const;

    std::string getUniqueID() const;

    std::string getPhotographLink() const;

    int getPrice() const;

    int getQuantity() const;

    void setUniqueID(const std::string& uniqueID);

    void setQuantity(int quantity);

    Coat& operator=(const Coat& otherCoat);

    bool operator==(const Coat& otherCoat);

    bool operator==(const std::string &sCoatID);

    bool operator!=(const Coat& otherCoat);

    friend std::ostream& operator<<(std::ostream& outStream, const Coat& coat);

    friend std::istream& operator>>(std::istream& inputStream, Coat& coat);
};


#endif //REDONICE_COAT_H
