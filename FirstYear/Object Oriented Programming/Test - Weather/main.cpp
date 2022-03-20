//
// Created by Teo on 5/24/2021.
//
#include <QApplication>
#include "Repository/RepositoryWeather.h"
#include "Service/ServiceWeather.h"
#include "GUI.h"


int main(int argc, char** argv) {
    QApplication a(argc, argv);
    RepositoryWeather repositoryWeather{};
    ServiceWeather serviceWeather{repositoryWeather};
    GUI someGui{serviceWeather};
    someGui.show();
    return a.exec();
}
