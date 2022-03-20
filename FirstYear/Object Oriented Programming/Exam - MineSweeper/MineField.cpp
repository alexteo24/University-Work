//
// Created by Teo on 7/7/2021.
//

#include "MineField.h"

MineField::MineField() {
    turn = 0;
    std::fstream fin("../input.txt");
    fin>>dimension;
    fin>>nrMines;
    for(int i = 0; i < 4;i++) {
        std::string playerName;
        fin>>playerName;
        players.push_back(playerName);
    }
    field = new int*[dimension + 2];
    for(int i = 0; i < dimension + 2; i++) {
        field[i] = new int[dimension + 2];
    }
    for(int i = 0; i < dimension + 2; i++) {
        for(int j = 0 ; j < dimension + 2; j++) {
            field[i][j] = 0;
        }
    }
    int rowAddition[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
    int columnAddition[8] = {0, 1, 1, 1, 0, -1, -1, -1};
    int i = 0;
    markedCells = 0;
    while(i != nrMines) {
        int rowMine = rand() % dimension + 1;
        int colMine = rand() % dimension + 1;
        while(field[rowMine][colMine] == -1) {
            rowMine = rand() % dimension + 1;
            colMine = rand() % dimension + 1;
        }
        field[rowMine][colMine] = -1;
        bombs.push_back(std::pair<int,int>(rowMine, colMine));
        i++;
    }
    for(auto& pair:bombs) {
        int row = pair.first;
        int column = pair.second;
        for(int j = 0 ; j < 8; j++) {
            if(field[row + rowAddition[j]][column + columnAddition[j]] != -1) {
                field[row + rowAddition[j]][column + columnAddition[j]]++;
            }
        }
    }
    displayField = new int*[dimension + 2];
    for(int h = 0; h < dimension + 2; h++) {
        displayField[h] = new int[dimension + 2];
    }
    for(int h = 0; h < dimension + 2; h++) {
        for(int j = 0 ; j < dimension + 2; j++) {
            displayField[h][j] = -2;
        }
    }
    this->notify();
}

int MineField::getDimension() const {
    return dimension;
}

int MineField::getNrMines() const {
    return nrMines;
}

std::vector<std::string> &MineField::getPlayers() {
    return players;
}

int **MineField::getMinefield() const{
    return field;
}

void MineField::attemptMove(int row, int column) {
    if(displayField[row][column] >= 0) {
        // Already displayed;
        throw MyException("Cell already played!");
    }
    if(field[row][column] == -1) {
        // hit a bomb, game over
        players.erase(players.begin() + turn);
        if(players.empty()) {
            throw MyException("Game over for all of you!");
        }
        turn = turn % (players.size());
        this->notify();
        throw MyException("You hit a bomb, you are out of the game!");
    }
    if(field[row][column] == -3) {
        throw MyException("Marked cell!");
    }
    displayField[row][column] = field[row][column];
    turn = (turn + 1) % players.size();
    this->notify();
}

int **MineField::getDisplayField() const{
    return displayField;
}

int MineField::getTurn() const {
    return turn;
}

void MineField::attemptMark(int row, int column) {
    if(displayField[row][column] == -3) {
        //cell marked => will unmark
        markedCells--;
        if(field[row][column] == -1) {
            //bomb
            auto it = std::find(bombs.begin(), bombs.end(), std::pair<int,int>(row, column));
            if(it == bombs.end()) {
                //re add bomb
                bombs.push_back(std::pair<int, int>(row, column));
            }
        }
        displayField[row][column] = -2;
        turn = (turn + 1) % players.size();
        this->notify();
        return;
    }
    if(displayField[row][column] == -2) {
        //good for marking
        markedCells++;
        if(field[row][column] == -1) {
            //bomb
            auto it = std::find(bombs.begin(), bombs.end(), std::pair<int,int>(row, column));
            bombs.erase(it);
        }
        displayField[row][column] = -3;
        turn = (turn + 1) % players.size();
        this->notify();
        return;
    }
    //revealed cell
    throw MyException("Cell was revealed!");
}

