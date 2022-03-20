//
// Created by Teo on 7/7/2021.
//

#include "GUI.h"

GUI::GUI(const std::string &player, MineField& mineField1): playerName{player}, mineField{mineField1} {
    mineField.addObserver(this);
    initGUI();
    populateTable();
    update();
    connectionAndSlots();
}

void GUI::initGUI() {
    setWindowTitle(QString::fromStdString(playerName));
    tableView = new QTableView{};
    std::vector<std::string> vector;
    tableModel = new TableModel{mineField};
    tableView->setModel(tableModel);
    QVBoxLayout* mainLayout = new QVBoxLayout{this};
    mainLayout->addWidget(tableView);
    setMinimumHeight(930);
    setMinimumWidth(930);
    tableView->horizontalHeader()->setDefaultSectionSize(75 );
    tableView->verticalHeader()->setDefaultSectionSize(75);
    tableView->setSelectionMode(QAbstractItemView::SingleSelection);

    QHBoxLayout* buttonsLayout = new QHBoxLayout{};
    revealButton = new QPushButton{"Reveal"};
    markMine = new QPushButton{"Mark mine"};
    buttonsLayout->addWidget(revealButton);
    buttonsLayout->addWidget(markMine);

    mainLayout->addLayout(buttonsLayout);

    show();
}

void GUI::connectionAndSlots() {
    QObject::connect(revealButton, &QPushButton::clicked, this, &GUI::revealCell);
    QObject::connect(markMine, &QPushButton::clicked, this, &GUI::markCell);
}

void GUI::update() {
    populateTable();
    if(mineField.getPlayers()[mineField.getTurn()] != playerName) {
        revealButton->setDisabled(true);
        markMine->setDisabled(true);
    } else {
        revealButton->setEnabled(true);
        markMine->setEnabled(true);
    }
    if(mineField.getBombs().empty() && mineField.getMarkedCells() == mineField.getNrMines()) {
        QMessageBox::about(this,"Congratulations", "You won, woop woop!");
        close();
    }
}

void GUI::populateTable() {
    tableView->setModel(nullptr);
    tableView->setModel(tableModel);
}

void GUI::revealCell() {
    int column = selectedColumn();
    int row = selectedRow() + 1;
    if(row == 0 || column == -1) {
        QMessageBox::critical(this, "Error", "Invalid play cell!");
        return;
    }
    try {
        mineField.attemptMove(row, column);
    } catch (MyException &ex) {
        if (strcmp(ex.what(), "You hit a bomb, you are out of the game!") == 0) {
            mineField.removeObserver(this);
            QMessageBox::critical(this, "Game over", ex.what());
            this->close();
            }
        if (strcmp(ex.what(), "Cell already played!") == 0) {
            QMessageBox::information(this, "Invalid cell", ex.what());
            return;
        }
        if (strcmp(ex.what(), "Game over for all of you!") == 0) {
            QMessageBox::information(this, "Invalid cell", ex.what());
            close();
        }
    }

}

void GUI::markCell() {
    int column = selectedColumn();
    int row = selectedRow() + 1;
    try {
        mineField.attemptMark(row, column);
    } catch (MyException &ex) {
//        if (strcmp(ex.what(), "You hit a bomb, you are out of the game!") == 0) {
//            auto it = std::find(mineField.getPlayers().begin(), mineField.getPlayers().end(), playerName);
//            mineField.getPlayers().erase(it);
//            QMessageBox::critical(this, "Game over", ex.what());
//            this->close();
//        }
        if (strcmp(ex.what(), "Cell was revealed!") == 0) {
            QMessageBox::information(this, "Invalid cell", ex.what());
            return;
        }
    }
    update();
}

int GUI::selectedColumn() {
    QModelIndexList selectedIndexes = tableView->selectionModel()->selectedIndexes();
    if(selectedIndexes.isEmpty()) {
        return -1;
    }
    int selectedIndex = selectedIndexes.at(0).column();
    std::cout<<selectedIndex<<"column\n";
    return selectedIndex;
}

int GUI::selectedRow() {
    QModelIndexList selectedIndexes = tableView->selectionModel()->selectedIndexes();
    if(selectedIndexes.isEmpty()) {
        return -1;
    }
    int selectedIndex = selectedIndexes.at(0).row();
    std::cout<<selectedIndex<<"row\n";
    return selectedIndex;
}
