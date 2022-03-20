//
// Created by Teo on 3/16/2021.
//

#include <iomanip>
#include "Coat.h"
using namespace std;

Coat::Coat(const std::string &size, const std::string &color, int price, int quantity, const std::string &photographLink,
           const std::string &uniqueID): size(size), color(color), price(price), quantity(quantity),
                                        photographLink(photographLink), uniqueID(uniqueID){}

Coat::Coat(const Coat &otherCoat): size(otherCoat.size), color(otherCoat.color), price(otherCoat.price),
                                         quantity(otherCoat.quantity), photographLink(otherCoat.photographLink),
                                         uniqueID(otherCoat.uniqueID){}

void Coat::setSize(const std::string &theSize) {
    size = theSize;
}

void Coat::setColor(const std::string &theColor) {
    color = theColor;
}

void Coat::setPrice(int thePrice) {
    price = thePrice;
}

void Coat::setQuantity(int theQuantity) {
    quantity = theQuantity;
}

void Coat::setPhotographLink(const std::string &thePhotographLink) {
    photographLink = thePhotographLink;
}

void Coat::setUniqueID(const std::string &theUniqueID) {
    uniqueID = theUniqueID;
}

string Coat::getSize() const{
    return size;
}

string Coat::getColour() const{
    return color;
}

int Coat::getPrice() {
    return price;
}

int Coat::getQuantity() {
    return quantity;
}

string Coat::getPhotographLink() const{
    return photographLink;
}

string Coat::getUniqueID() const{
    return uniqueID;
}

Coat & Coat::operator=(const Coat &otherCoat) = default;

bool Coat::operator==(const Coat &otherCoat) {
    return uniqueID == otherCoat.uniqueID;
}

bool Coat::operator!=(const Coat &otherCoat) {
    return uniqueID != otherCoat.uniqueID;
}

std::ostream &operator <<(std::ostream &output, const Coat &Coat) {
    output <<std::left << std::setw(5) << Coat.size << std::setw(15) << Coat.color << std::setw(10) << Coat.price
          << std::setw(5) << Coat.quantity << std::setw(15) << Coat.uniqueID << std::setw(5)<<
          Coat.photographLink << '\n';
    return output;
}