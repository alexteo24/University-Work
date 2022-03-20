//
// Created by Teo on 5/24/2021.
//

#include "Weather.h"
#include <vector>
#include <sstream>

Weather::Weather(): _startHour{-1}, _endHour{-1}, _precipitationProbability{-1}, _description{} {
}

Weather::Weather(const int startHour, const int endHour, const int precipitationProbability,
                 const std::string &description): _startHour{startHour}, _endHour{endHour}, _precipitationProbability{precipitationProbability},
                 _description{description} {

}

std::vector<std::string> tokenize(const std::string& str, char delimiter) {
    std::vector<std::string> result;
    std::stringstream ss(str);
    std::string token;
    while (getline(ss, token, delimiter))
        result.push_back(token);

    return result;
}

std::istream &operator>>(std::istream &is, Weather &sWeather) {
    std::string line;
    getline(is, line);

    std::vector<std::string> tokens = tokenize(line, ';');
    if (tokens.size() != 4)
        return is;
    sWeather._startHour = stoi(tokens[0]);
    sWeather._endHour = stoi(tokens[1]);
    sWeather._precipitationProbability = stoi(tokens[2]);
    sWeather._description = tokens[3];
    return is;
}