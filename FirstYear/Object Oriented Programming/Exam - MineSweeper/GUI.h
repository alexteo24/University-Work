//
// Created by Teo on 7/7/2021.
//

#ifndef E3_ALEXTEO24_GUI_H
#define E3_ALEXTEO24_GUI_H
#include "Observer.h"
#include <QWidget>
#include "TableModel.h"
#include "MineField.h"
#include <QMessageBox>
#include <QPushButton>
#include <QVBoxLayout>
#include <QTableView>
#include <iostream>
#include <QHeaderView>
#include <cstring>
#include <ctime>
#include <algorithm>

class GUI: public QWidget, public Observer {
private:
    std::string playerName;
    MineField& mineField;
    QTableView* tableView;
    TableModel* tableModel;
    QPushButton* revealButton;
    QPushButton* markMine;

public:
    GUI(const std::string& player, MineField& mineField1);
    void initGUI();
    void populateTable();
    void connectionAndSlots();
    void update() override;
    void revealCell();
    void markCell();
    int selectedColumn();
    int selectedRow();
};


#endif //E3_ALEXTEO24_GUI_H
