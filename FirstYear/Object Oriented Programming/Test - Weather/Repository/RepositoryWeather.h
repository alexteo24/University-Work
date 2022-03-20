//
// Created by Teo on 5/24/2021.
//

#ifndef T3_ALEXTEO24_REPOSITORYWEATHER_H
#define T3_ALEXTEO24_REPOSITORYWEATHER_H
#include "../Domain/Weather.h"
#include <vector>

class RepositoryWeather {
private:
    std::string _fileName;
    std::vector<Weather> _weatherList;

public:
    RepositoryWeather(const std::string& fileName = "input.txt");
    ~RepositoryWeather() = default;
    void readData();
    void addNewWeather(const Weather& newWeather);
    std::vector<Weather>& getVector() {return _weatherList;}
};


#endif //T3_ALEXTEO24_REPOSITORYWEATHER_H
