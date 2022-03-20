//
// Created by Teo on 4/11/2021.
//

#include "ValidatorCoat.h"

void ValidatorCoat::validateCoat(const std::string &size, const std::string &color, const std::string &uniqueID,
                                 const std::string &photographLink, int price, int quantity) {
    std::string exceptions;
    std::regex e ("[sml]{1}|[x]{1,3}[l]$", std::regex_constants::icase);
    if (size.length() == 0 || regex_match(size, e) == 0) {
        exceptions += "Invalid coat size!\n";
    }
    if (color.length() == 0) {
        exceptions += "Invalid coat color!\n";
    }
    if (uniqueID.length() != 7) {
        exceptions += "Invalid coat uniqueID!\n";
    }
    std::regex f ("^https://www\\.[a-z]+\\.[a-z]{2,3}$", std::regex_constants::icase);
    if (photographLink.length() == 0 || regex_match(photographLink, f) == 0) {
        exceptions += "Invalid coat photograph link!\n";
    }
    if (price <= 0) {
        exceptions += "Invalid coat price!\n";
    }
    if (quantity < 0) {
        exceptions += "Invalid coat quantity!\n";
    }
    if (exceptions.length() > 0) {
        throw ValidationException(exceptions);
    }
}

void ValidatorCoat::validateCoat(const Coat& sCoat) {
    std::string exceptions;
    std::regex e ("[sml]{1}|[x]{1,3}[l]$", std::regex_constants::icase);
    if (sCoat.getSize().length() == 0 || regex_match(sCoat.getSize(), e) == 0) {
        exceptions += "Invalid coat size!\n";
    }
    if (sCoat.getColor().length() == 0) {
        exceptions += "Invalid coat color!\n";
    }
    if (sCoat.getUniqueID().length() != 7) {
        exceptions += "Invalid coat uniqueID!\n";
    }
    std::regex f ("^https://www\\.[a-z]+\\.[a-z]{2,3}$", std::regex_constants::icase);
    if (sCoat.getPhotographLink().length() == 0 || regex_match(sCoat.getPhotographLink(), f) == 0) {
        exceptions += "Invalid coat photograph link!\n";
    }
    if (sCoat.getPrice() <= 0) {
        exceptions += "Invalid coat price!\n";
    }
    if (sCoat.getQuantity() < 0) {
        exceptions += "Invalid coat quantity!\n";
    }
    if (exceptions.length() > 0) {
        throw ValidationException(exceptions);
    }
}

ValidationException::ValidationException(const std::string &_message): message{_message} {}

const char *ValidationException::what() const noexcept {
    return message.c_str();
}
