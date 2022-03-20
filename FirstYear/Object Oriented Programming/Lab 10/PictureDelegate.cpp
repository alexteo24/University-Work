//
// Created by Teo on 5/31/2021.
//

#include "PictureDelegate.h"

void PictureDelegate::paint(QPainter *painter, const QStyleOptionViewItem &option, const QModelIndex &index) const {
    QString color = index.model()->data(index, Qt::DisplayRole).toString();
    // show a picture only in the second column; the other columns remain unchanged
    if (index.column() != 5)
    {
        QStyledItemDelegate::paint(painter, option, index);
        return;
    }

    std::string fileName = "../Pictures/index.jpg";
    if (color.contains("BLACK")) {
        fileName = "../Pictures/BLACK.jpg";
    }
    if (color.contains("BUTTERCREAM")) {
        fileName = "../Pictures/BUTTERCREAM.jpg";
    }
    if (color.contains("CHESTNUT")) {
        fileName = "../Pictures/CHESTNUT.jpg";
    }
    if (color.contains("COBALT")) {
        fileName = "../Pictures/COBALT.jpg";
    }
    if (color.contains("DARK BLUE")) {
        fileName = "../Pictures/DARK BLUE.jpg";
    }
    if (color.contains("FLAME")) {
        fileName = "../Pictures/FLAME.jpg";
    }
    if (color.contains("GRAY")) {
        fileName = "Pictures/GRAY.jpg";
    }
    if (color.contains("GREEN")) {
        fileName = "../Pictures/GREEN.jpg";
    }
    if (color.contains("LEOPARD")) {
        fileName = "../Pictures/LEOPARD.jpg";
    }
    if (color.contains("PURPLE")) {
        fileName = "../Pictures/PURPLE.jpg";
    }
    if (color.contains("RED")) {
        fileName = "../Pictures/RED.jpg";
    }
    QPixmap pixMap(QString::fromStdString(fileName));
    painter->drawPixmap(option.rect, pixMap);
}

QSize PictureDelegate::sizeHint(const QStyleOptionViewItem &option, const QModelIndex &index) const {

    if (index.column() == 5)
    {
        return QSize(50, 100);
    }

    return QStyledItemDelegate::sizeHint(option, index);
}

PictureDelegate::PictureDelegate(QWidget *parent): QStyledItemDelegate{parent} {}
