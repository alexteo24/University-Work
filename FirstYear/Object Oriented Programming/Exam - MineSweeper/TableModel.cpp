//
// Created by misu on 07/07/2021.
//

#include "TableModel.h"
#include <QBrush>
#include <QColor>
TableModel::~TableModel() {

}

int TableModel::rowCount(const QModelIndex &parent) const {
    return mineField.getDimension();
}

int TableModel::columnCount(const QModelIndex &parent) const {
    return mineField.getDimension() + 1;
}

QVariant TableModel::data(const QModelIndex &index, int role) const {
    int row = index.row();
    int column = index.column();
    if (row == mineField.getDimension()) {
        return QVariant{};
    }
    int** displayField = mineField.getDisplayField();
    int** field = mineField.getMinefield();
    if (role == Qt::DisplayRole) {
        if(column == 0)
            return QString::number(row + 1);
        else if(column <=columnCount()) {
            if(displayField[row + 1][column] == -3) {
                return QString("*");
            }
            if(displayField[row + 1][column] == -2) {
                // not hit or anything
                return QString("");
            }
            if(displayField[row + 1][column] >= 0) {
                //hit
                return QString::number(field[row + 1][column]);
            }

        }
    }
    if (role == Qt::BackgroundRole) {
        if(displayField[row + 1][column] == -2) {
            //not played
            return QBrush{QColor{100, 255, 100}};
        }
        if(displayField[row + 1][column] == -3) {
            //marked
            return QBrush{QColor{255, 100, 100}};
        }
        if(displayField[row + 1][column] >= 0) {
            //played
            return QBrush{QColor{100, 100, 255}};
        }

    }
    else if(role == Qt::SizeHintRole) {
        return QSize(100, 100);
    }
    return QVariant{};
}



QVariant TableModel::headerData(int section, Qt::Orientation orientation, int role) const {
    if (role == Qt::DisplayRole || role == Qt::EditRole) {

        if (orientation == Qt::Horizontal) {
            if(section == 0)
                return QString("");
            else
                if(section <= rowCount())
                    return QString('A' + section-1);
        }
    }
    if(role == Qt::SizeHintRole) {
        return QSize(0, 100);
    }


    return QVariant();
}

bool TableModel::setData(const QModelIndex &index, const QVariant &value, int role) {
    return QAbstractItemModel::setData(index, value, role);
}

Qt::ItemFlags TableModel::flags(const QModelIndex &index) const {
    return QAbstractTableModel::flags(index);
}

void TableModel::update_internal_data() {

}
