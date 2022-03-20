//
// Created by Teo on 5/30/2021.
//

#ifndef A10_ALEXTEO24_TABELMODEL_H
#define A10_ALEXTEO24_TABELMODEL_H
#include <QAbstractTableModel>
#include "../RepositoryShopping/RepostioryShopping.h"
#include "../ServiceUser/ServiceUser.h"

class TableModel: public QAbstractTableModel {
private:
    ServiceUser& _serviceUser;

public:
    TableModel(ServiceUser& serviceUser, QObject *parent = nullptr);

    ~TableModel() = default;

    int rowCount(const QModelIndex &parent = QModelIndex{}) const override;

    int columnCount(const QModelIndex &parent = QModelIndex{}) const override;

    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;

    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override;

};


#endif //A10_ALEXTEO24_TABELMODEL_H
