//
// Created by Teo on 5/24/2021.
//

#include "ServiceWeather.h"
#include <algorithm>

ServiceWeather::ServiceWeather(RepositoryWeather &repositoryWeather):_repoWeather{repositoryWeather}, _existingWeatherDescriptions{}, _existingDescriptions{} {}

std::vector<Weather> ServiceWeather::getLessThanProbability(int probability) {
    std::vector<Weather> weatherList;
    for(auto& i : _repoWeather.getVector()) {
        if (i.getPrecipitationProbability() < probability){
            weatherList.push_back(i);
        }
    }
    return weatherList;
}

void ServiceWeather::addNewDescription(const std::string &description) {
    auto it = std::find(_existingWeatherDescriptions.begin(), _existingWeatherDescriptions.end(), description);
    if (it == _existingWeatherDescriptions.end())
        _existingWeatherDescriptions.push_back(description);
}

void ServiceWeather::removeDescription(const std::string &description) {
    auto it = std::find(_existingWeatherDescriptions.begin(), _existingWeatherDescriptions.end(), description);
    if (it != _existingWeatherDescriptions.end()) {
        _existingWeatherDescriptions.erase(it);
    }
}

void ServiceWeather::determineExistingDescriptions() {
    for(auto& i:getVector()) {
        bool found = false;
        for(auto& j:_existingDescriptions) {
            if(j == i.getDescription()) {
                found = true;
                break;
            }
        }
        if(!found) {
            _existingDescriptions.push_back(i.getDescription());
        }
    }
}
