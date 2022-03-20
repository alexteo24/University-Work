//
// Created by Teo on 4/11/2021.
//
#pragma once
#ifndef REDONICE_VALIDATORCOAT_H
#define REDONICE_VALIDATORCOAT_H
#include <string>
#include <regex>
#include <exception>
#include "../Domain/Coat.h"


class ValidatorCoat {
public:
    static void validateCoat(const std::string& size, const std::string& color, const std::string& uniqueID,
                             const std::string& photographLink, int price, int quantity);

    static void validateCoat(const Coat& sCoat);
};

class ValidationException : public std::exception {
private:
    std::string message;

public:
    ValidationException(const std::string& _message);

    const char *what() const noexcept override;
};


#endif //REDONICE_VALIDATORCOAT_H
