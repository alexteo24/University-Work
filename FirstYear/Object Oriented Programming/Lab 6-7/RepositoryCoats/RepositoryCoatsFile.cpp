//
// Created by Teo on 4/11/2021.
//

#include "RepositoryCoatsFile.h"
#include <fstream>

RepositoryCoatsFile::RepositoryCoatsFile() : RepositoryCoats{} { readDataFromFile("../RepoFile.txt");}

void RepositoryCoatsFile::readDataFromFile(const std::string &fileName) {
    std::fstream fin(fileName);
    Coat sCoat;
    while (fin>>sCoat) {
        try {
            ValidatorCoat::validateCoat(sCoat);
            RepositoryCoats::addCoatRepo(sCoat);
        } catch(std::exception&){
            throw RepositoryCoatsException("Duplicate coats or invalid coat data stored in the database!");
        }
    }
    fin.close();
}

void RepositoryCoatsFile::writeDataToFile(const std::string &fileName) {
    std::ofstream fout(fileName, std::ofstream::trunc);
    std::string string;
    for(const Coat& i : getVector()) {
        string += i.getSize() + ";" + i.getColor() + ";" + i.getUniqueID() + ";" + i.getPhotographLink() + ";" +
                std::to_string(i.getPrice()) + ";" + std::to_string(i.getQuantity()) + "\n";
        fout<<string;
        string = "";
    }
    fout.close();
}

void RepositoryCoatsFile::addCoatRepo(const Coat &sCoat) {
    RepositoryCoats::addCoatRepo(sCoat);
    writeDataToFile("../RepoFile.txt");
}

void RepositoryCoatsFile::deleteCoatRepo(const std::string &sCoatID) {
    RepositoryCoats::deleteCoatRepo(sCoatID);
    writeDataToFile("../RepoFile.txt");
}

void RepositoryCoatsFile::updateCoatRepo(const Coat &sCoat) {
    RepositoryCoats::updateCoatRepo(sCoat);
    writeDataToFile("../RepoFile.txt");
}

std::vector<Coat> &RepositoryCoatsFile::getVector() {
    return RepositoryCoats::getVector();
}

RepositoryCoatsFile::~RepositoryCoatsFile() {
    writeDataToFile("../RepoFile.txt");
}