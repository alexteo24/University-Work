//
// Created by Teo on 5/31/2021.
//

#ifndef A10_ALEXTEO24_PICTUREDELEGATE_H
#define A10_ALEXTEO24_PICTUREDELEGATE_H
#include <QStyledItemDelegate>
#include <QPainter>
#include <QPixmap>

class PictureDelegate: public QStyledItemDelegate {
public:
    PictureDelegate(QWidget *parent = 0);

    // these two functions need to be overridden to draw an image for each item
    void paint(QPainter *painter, const QStyleOptionViewItem &option, const QModelIndex &index) const override;

    QSize sizeHint(const QStyleOptionViewItem &option,const QModelIndex &index) const override;
};


#endif //A10_ALEXTEO24_PICTUREDELEGATE_H
