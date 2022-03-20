//
// Created by Teo on 5/24/2021.
//

#ifndef T3_ALEXTEO24_SERVICEWEATHER_H
#define T3_ALEXTEO24_SERVICEWEATHER_H
#include "../Repository/RepositoryWeather.h"

class ServiceWeather {
private:
    RepositoryWeather& _repoWeather;
    std::vector<std::string> _existingWeatherDescriptions;
    std::vector<std::string> _existingDescriptions;

public:
    ServiceWeather(RepositoryWeather& repositoryWeather);
    ~ServiceWeather() = default;
    void addNewDescription(const std::string& description);
    void removeDescription(const std::string& description);
    void determineExistingDescriptions();
    std::vector<std::string>& getExistingDescriptions() {return _existingDescriptions;}
    std::vector<Weather>& getVector() {return _repoWeather.getVector();}
    std::vector<std::string>& getDescriptions() {return _existingWeatherDescriptions;}
    std::vector<Weather> getLessThanProbability(int probability);
};


#endif //T3_ALEXTEO24_SERVICEWEATHER_H
