//
// Created by Teo on 4/11/2021.
//

#include "ExceptionsRepoCoats.h"

RepositoryCoatsException::RepositoryCoatsException(const std::string &_message) : _message{_message}{}

const char *RepositoryCoatsException::what() const noexcept {
    return _message.c_str();
}
