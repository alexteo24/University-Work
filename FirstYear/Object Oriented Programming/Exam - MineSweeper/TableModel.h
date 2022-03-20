//
// Created by misu on 07/07/2021.
//

#ifndef MINESWEEPER_TABLEMODEL_H
#define MINESWEEPER_TABLEMODEL_H

#include <QAbstractTableModel>
#include "MineField.h"

class TableModel: public QAbstractTableModel {
private:
    MineField mineField;
public:
    explicit TableModel(MineField& field, QObject* parent = NULL): mineField{field}, QAbstractTableModel{parent} {};

    ~TableModel();

    int rowCount(const QModelIndex &parent = QModelIndex()) const override;

    int columnCount(const QModelIndex &parent = QModelIndex()) const override;

    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const;

    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const;

    bool setData(const QModelIndex &index, const QVariant &value, int role = Qt::EditRole) override;

    Qt::ItemFlags flags(const QModelIndex &index) const;

    void update_internal_data();
};


#endif //MINESWEEPER_TABLEMODEL_H
