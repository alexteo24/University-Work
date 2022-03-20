//
// Created by Teo on 4/12/2021.
//

#include "ShoppingExceptions.h"

ShoppingException::ShoppingException(const std::string &message) : _message(message){}

const char *ShoppingException::what() const noexcept {
    return _message.c_str();
}
