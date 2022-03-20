//
// Created by Teo on 5/24/2021.
//

#include "GUI.h"

GUI::GUI(ServiceWeather &serviceWeather): _serviceWeather{serviceWeather}, _checkBoxes{} {
    initGUI();
    populateList();
    connectSignalsAndSlots();
}

void GUI::initGUI() {
    QVBoxLayout* mainLayout = new QVBoxLayout{this};
    _greetingsLabel = new QLabel{"This is the weather for today"};
    _weathersListWidget = new QListWidget{};
    mainLayout->addWidget(_greetingsLabel);
    mainLayout->addWidget(_weathersListWidget);
    _precipitationSlider = new QSlider{Qt::Horizontal};
    _precipitationSlider->setRange(0, 100);
    _precipitationSlider->setValue(100);
    _sliderValue = new QLabel{"100"};
    QHBoxLayout* sliderLayout = new QHBoxLayout{};
    _sliderValue->setBuddy(_precipitationSlider);
    sliderLayout->addWidget(_sliderValue);
    sliderLayout->addWidget(_precipitationSlider);
    mainLayout->addLayout(sliderLayout);
    QHBoxLayout* checkBoxesLayout = new QHBoxLayout{};
    _serviceWeather.determineExistingDescriptions();
    for(auto& i:_serviceWeather.getExistingDescriptions()) {
        QCheckBox* newCheckBox = new QCheckBox{QString::fromStdString(i)};
        _checkBoxes.push_back(newCheckBox);
        checkBoxesLayout->addWidget(newCheckBox);
    }
//    _overcastCheckBox = new QCheckBox{"Overcast"};
//    _foggyCheckBox = new QCheckBox{"Foggy"};
//    _sunnyCheckBox = new QCheckBox{"Sunny"};
//    _rainCheckBox = new QCheckBox{"Rain"};
//    _thunderstormCheckBox = new QCheckBox{"Thunderstorm"};
//    checkBoxesLayout->addWidget(_overcastCheckBox);
//    checkBoxesLayout->addWidget(_foggyCheckBox);
//    checkBoxesLayout->addWidget(_sunnyCheckBox);
//    checkBoxesLayout->addWidget(_rainCheckBox);
//    checkBoxesLayout->addWidget(_thunderstormCheckBox);
    mainLayout->addLayout(checkBoxesLayout);
    _resetButton = new QPushButton{"Reset filters"};
    mainLayout->addWidget(_resetButton);
}

void GUI::populateList() {
    _weathersListWidget->clear();
    int probability = _precipitationSlider->value();
    if (probability == 100) {
        probability++;
    }
    for(auto& i:_serviceWeather.getLessThanProbability(probability)) {
        _weathersListWidget->addItem(QString::fromStdString("From " + std::to_string(i.getStartHour()) + " to "
        + std::to_string(i.getEndHour()) + " the weather will be " + i.getDescription() + " with the chance "
        + std::to_string(i.getPrecipitationProbability()) + "% of precipitations"));
    }
}

void GUI::connectSignalsAndSlots() {
    QObject::connect(_precipitationSlider, &QSlider::valueChanged, this, &GUI::filterProbability);
    QObject::connect(_resetButton, &QPushButton::clicked, this, &GUI::resetFilters);
    for(auto& i : _checkBoxes) {
        QObject::connect(i, &QPushButton::clicked, this, &GUI::checkBoxClicked);
    }
}

void GUI::filterProbability() {
    _sliderValue->setText(QString::fromStdString(std::to_string(_precipitationSlider->value())));
    checkBoxClicked();
}

void GUI::resetFilters() {
    for(auto& i : _checkBoxes) {
        i->setCheckState(Qt::Unchecked);
    }
//    _overcastCheckBox->setCheckState(Qt::Unchecked);
//    _foggyCheckBox->setCheckState(Qt::Unchecked);
//    _sunnyCheckBox->setCheckState(Qt::Unchecked);
//    _rainCheckBox->setCheckState(Qt::Unchecked);
//    _thunderstormCheckBox->setCheckState(Qt::Unchecked);
    _precipitationSlider->setValue(100);
    populateList();
}

void GUI::checkBoxClicked() {
    _weathersListWidget->clear();
    for(auto & i :_checkBoxes) {
        if(i->isChecked()) {
            _serviceWeather.addNewDescription(i->text().toStdString());
        } else {
            _serviceWeather.removeDescription(i->text().toStdString());
        }
    }
    if (_serviceWeather.getDescriptions().empty()) {
        populateList();
    } else {
        for (auto &j :_serviceWeather.getDescriptions()) {
            for (auto &k : _serviceWeather.getVector()) {
                if (k.getDescription() == j) {
                    if (_precipitationSlider->value() > k.getPrecipitationProbability()) {
                        _weathersListWidget->addItem(
                                QString::fromStdString("From " + std::to_string(k.getStartHour()) + " to "
                                                       + std::to_string(k.getEndHour()) + " the weather will be " +
                                                       k.getDescription() + " with the chance "
                                                       + std::to_string(k.getPrecipitationProbability()) +
                                                       "% of precipitations"));
                    }
                }
            }
        }
    }
}
