//
// Created by Teo on 7/7/2021.
//

#ifndef E3_ALEXTEO24_MINEFIELD_H
#define E3_ALEXTEO24_MINEFIELD_H
#include <vector>
#include <string>
#include <fstream>
#include <random>
#include <exception>
#include "Observer.h"

class MyException: public std::exception {
private:
    std::string message;
public:
    MyException(const std::string& message): message{message} {}
    const char* what() const noexcept override {return message.c_str();}
};

class MineField: public Observable{
private:
    int dimension;
    int nrMines;
    int turn;
    int **field;
    int **displayField;
    int markedCells;
    std::vector<std::pair<int, int>> bombs;
    std::vector<std::string> players;

public:
    MineField();
    int getDimension() const;
    int getNrMines() const;
    int getTurn() const;
    std::vector<std::string>& getPlayers();
    int** getMinefield() const;
    int** getDisplayField() const;
    void attemptMove(int row, int column);
    void attemptMark(int row, int column);
    int getMarkedCells() const { return markedCells;}
    std::vector<std::pair<int,int>>& getBombs() {return bombs;}
};


#endif //E3_ALEXTEO24_MINEFIELD_H
