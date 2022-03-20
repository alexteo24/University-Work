//
// Created by Teo on 5/24/2021.
//

#ifndef T3_ALEXTEO24_GUI_H
#define T3_ALEXTEO24_GUI_H
#include <QWidget>
#include <QListWidget>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QGridLayout>
#include <QLabel>
#include <QPushButton>
#include <QSlider>
#include <QCheckBox>
#include "Service/ServiceWeather.h"
#include <vector>

class GUI: public QWidget{
private:
    ServiceWeather& _serviceWeather;
    QListWidget* _weathersListWidget;
    QLabel* _greetingsLabel, *_sliderValue;
    QSlider* _precipitationSlider;
    QCheckBox* _overcastCheckBox, *_foggyCheckBox, *_sunnyCheckBox, *_rainCheckBox, *_thunderstormCheckBox;
    QPushButton* _resetButton;
    std::vector<QCheckBox*> _checkBoxes;

public:
    GUI(ServiceWeather& serviceWeather);
    void initGUI();
    void populateList();
    void connectSignalsAndSlots();
    void filterProbability();
    void resetFilters();
    void checkBoxClicked();
};


#endif //T3_ALEXTEO24_GUI_H
