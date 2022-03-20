//
// Created by Teo on 3/31/2021.
//

#include "Coat.h"
#include "iomanip"
#include <sstream>
#include <vector>

Coat::Coat():_size{""}, _color{""}, _uniqueID{""}, _photographLink{""}, _price {-1}, _quantity{-1}{}

Coat::Coat(const std::string &size, const std::string &color, const std::string &uniqueID,
           const std::string &photographLink, int price, int quantity):_size{size}, _color{color}, _uniqueID{uniqueID},
                                                                            _photographLink{photographLink},
                                                                            _price{price}, _quantity{quantity} {}

Coat::Coat(const Coat &otherCoat):_size{otherCoat._size}, _color{otherCoat._color}, _uniqueID{otherCoat._uniqueID},
                                    _photographLink{otherCoat._photographLink}, _price{otherCoat._price},
                                    _quantity{otherCoat._quantity} {}

std::string Coat::getSize() const {
    return _size;
}

std::string Coat::getColor() const {
    return _color;
}

std::string Coat::getUniqueID() const {
    return _uniqueID;
}

std::string Coat::getPhotographLink() const {
    return _photographLink;
}

int Coat::getPrice() const {
    return _price;
}

int Coat::getQuantity() const {
    return _quantity;
}

void Coat::setUniqueID(const std::string &uniqueID) {
    _uniqueID = uniqueID;
}

Coat& Coat::operator=(const Coat &otherCoat) {
    _size = otherCoat._size;
    _color = otherCoat._color;
    _uniqueID = otherCoat._uniqueID;
    _photographLink = otherCoat._photographLink;
    _price = otherCoat._price;
    _quantity = otherCoat._quantity;
    return *this;
}

bool Coat::operator==(const Coat &otherCoat) {
    return _uniqueID == otherCoat._uniqueID;
}

bool Coat::operator==(const std::string &sCoatID) {
    return _uniqueID == sCoatID;
}

bool Coat::operator!=(const Coat &otherCoat) {
    return _uniqueID != otherCoat._uniqueID;
}

std::vector<std::string> tokenize(const std::string& str, char delimiter) {
    std::vector<std::string> result;
    std::stringstream ss(str);
    std::string token;
    while (getline(ss, token, delimiter))
        result.push_back(token);

    return result;
}

std::istream &operator>>(std::istream &is, Coat &sCoat) {
    std::string line;
    getline(is, line);

    std::vector<std::string> tokens = tokenize(line, ';');
    if (tokens.size() != 6)
        return is;
    sCoat._size = tokens[0];
    sCoat._color = tokens[1];
    sCoat._uniqueID = tokens[2];
    sCoat._photographLink = tokens[3];
    std::stringstream ss;
    ss << tokens[4];
    ss >> sCoat._price;
    ss.clear();
    ss << tokens[5];
    ss >> sCoat._quantity;
    ss.clear();
    return is;
}

std::ostream &operator <<(std::ostream &output, const Coat &Coat) {
    output << Coat._size << "," << Coat._color << "," << Coat._price << "," << Coat._quantity << ","
            << Coat._uniqueID << "," << Coat._photographLink;
    return output;
}

void Coat::setQuantity(int quantity) {
    _quantity = quantity;
}
