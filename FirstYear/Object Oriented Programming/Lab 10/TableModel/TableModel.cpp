//
// Created by Teo on 5/30/2021.
//

#include "TableModel.h"

TableModel::TableModel(ServiceUser &serviceUser, QObject *parent): _serviceUser{serviceUser} {

}

int TableModel::rowCount(const QModelIndex &parent) const {
    return _serviceUser.getCartForPrint().size();
}

int TableModel::columnCount(const QModelIndex &parent) const {
    return 6;
}

QVariant TableModel::data(const QModelIndex &index, int role) const {
    int row = index.row();
    int column = index.column();
    if (row == _serviceUser.getCartForPrint().size()) {
        return QVariant{};
    }
    Coat sCoat = _serviceUser.getCartForPrint()[row];
    if (role == Qt::DisplayRole) {
        switch (column) {
            case 0:
                return QString::fromStdString(sCoat.getSize());
            case 1:
                return QString::fromStdString(sCoat.getColor());
            case 2:
                return QString::fromStdString(std::to_string(sCoat.getPrice()));
            case 3:
                return QString::fromStdString(std::to_string(sCoat.getQuantity()));
            case 4:
                return QString::fromStdString(sCoat.getPhotographLink());
            case 5:
                return QString::fromStdString(sCoat.getColor());
            case 6:
                return QVariant{};
            default:
                break;
        }
    }
    return QVariant{};
}

QVariant TableModel::headerData(int section, Qt::Orientation orientation, int role) const {
    if (role == Qt::DisplayRole) {
        if (orientation == Qt::Horizontal) {
            switch (section) {
                case 0:
                    return QString{"Size"};
                case 1:
                    return QString{"Color"};
                case 2:
                    return QString{"Price"};
                case 3:
                    return QString{"Quantity"};
                case 4:
                    return QString{"PhotographLink"};
                case 5:
                    return QString{"Photograph"};
                default:
                    break;
            }
        }
    }
    return QVariant{};
}
