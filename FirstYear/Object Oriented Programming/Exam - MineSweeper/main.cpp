//
// Created by Teo on 7/7/2021.
//

#include "MineField.h"
#include <iostream>
#include <QApplication>
#include <iostream>
#include "GUI.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    MineField mineField{};
    auto players = mineField.getPlayers();
    for(auto& player: players) {
        GUI* newWindow = new GUI{player, mineField};
    }
    std::cout<<"test";
    return QApplication::exec();
}