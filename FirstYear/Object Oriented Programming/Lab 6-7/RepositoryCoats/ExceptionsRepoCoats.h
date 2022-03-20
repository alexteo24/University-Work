//
// Created by Teo on 4/11/2021.
//
#pragma once
#ifndef REDONICE_EXCEPTIONSREPOCOATS_H
#define REDONICE_EXCEPTIONSREPOCOATS_H
#include <exception>
#include <string>

class RepositoryCoatsException : public std::exception
{
private:
    std::string _message;

public:
    RepositoryCoatsException(const std::string& _message);

    const char *what() const noexcept override;
};

#endif //REDONICE_EXCEPTIONSREPOCOATS_H
