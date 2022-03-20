//
// Created by Teo on 5/24/2021.
//

#ifndef T3_ALEXTEO24_WEATHER_H
#define T3_ALEXTEO24_WEATHER_H
#include <string>

class Weather {
private:
    int _startHour;
    int _endHour;
    int _precipitationProbability;
    std::string _description;

public:
    Weather();
    Weather(const int startHour, const int endHour, const int precipitationProbability, const std::string& description);
    ~Weather() = default;
    int getStartHour() const {return _startHour;}
    int getEndHour() const {return _endHour;}
    int getPrecipitationProbability() const {return _precipitationProbability;}
    std::string getDescription() const {return _description;}
    friend std::istream& operator>>(std::istream& inputStream, Weather& sWeather);
};


#endif //T3_ALEXTEO24_WEATHER_H
