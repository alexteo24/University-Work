//
// Created by Teo on 5/24/2021.
//

#include <fstream>
#include "RepositoryWeather.h"

RepositoryWeather::RepositoryWeather(const std::string &fileName): _weatherList{}, _fileName{fileName} {
    readData();
}

void RepositoryWeather::readData() {
    std::fstream fin("../" + _fileName);
    Weather sWeather;
    while (fin>>sWeather) {
        addNewWeather(sWeather);
    }
    fin.close();
}

void RepositoryWeather::addNewWeather(const Weather& newWeather) {
    _weatherList.push_back(newWeather);
}
