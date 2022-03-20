//
// Created by Teo on 4/12/2021.
//

#ifndef REDONICE_SHOPPINGEXCEPTIONS_H
#define REDONICE_SHOPPINGEXCEPTIONS_H
#include <exception>
#include <string>

class ShoppingException : public std::exception
{
private:
    std::string _message;

public:
    ShoppingException(const std::string& message);

    const char *what() const noexcept override;
};

#endif //REDONICE_SHOPPINGEXCEPTIONS_H
