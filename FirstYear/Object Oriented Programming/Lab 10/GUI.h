//
// Created by Teo on 5/1/2021.
//

#ifndef A89_ALEXTEO24_GUI_H
#define A89_ALEXTEO24_GUI_H
#include <QWidget>
#include <QListWidget>
#include <QPushButton>
#include <QLineEdit>
#include <QLabel>
#include <QMessageBox>
#include <QVBoxLayout>
#include <QFormLayout>
#include <QComboBox>
#include <QTableView>
#include <QtCharts/QPieSlice>
#include <QtCharts/QPieSeries>
#include <QShortcut>
#include <QtCharts/QChart>
#include <QAbstractTableModel>
#include <QtCharts/QChartView>
#include "TableModel/TableModel.h"
#include "ServiceUser/ServiceUser.h"
#include "ServiceAdmin/ServiceAdministrator.h"
#include "PictureDelegate.h"

class GUI: public QWidget{
private:
    ServiceAdministrator& _serviceAdministrator;
    ServiceUser& _serviceUser;
public:
    GUI(ServiceAdministrator& serviceAdministrator, ServiceUser& serviceUser);
    void initGUI();
};

class adminGUI: public QWidget{
private:
    ServiceAdministrator& _serviceAdministrator;
    QListWidget* coatsListWidget;
    QLineEdit* sizeLineEdit, *colorLineEdit, *uniqueIDLineEdit, *photographLinkLineEdit, *priceLineEdit, *quantityLineEdit;
    QPushButton* addButton, *deleteButton, *updateButton, *displayPieChartButton, *undoButton, *redoButton;

public:
    explicit adminGUI(ServiceAdministrator& serviceAdministrator);

    void initGUI();

    void populateList();

    void connectSignalsAndSlots();

    int getSelectedIndex();

    void addCoatOperation();

    void deleteCoatOperation();

    void updateCoatOperation();

    void displayStatistics();

    void undoOperation();

    void redoOperation();
};

class userGUI: public QWidget {
private:
    ServiceUser& _serviceUser;
    QLineEdit* coatSizeLineEdit, *coatColorLineEdit, *coatPriceLineEdit, *filterSizeLineEdit;
    QLabel* coatsListLabel, *shoppingBasketLabel, *totalCost;
    QPushButton* addCoatButton, *openShoppingBasketButton, *filterCoatsButton, *checkoutButton, *undoButton, *redoButton;
    QListWidget* coatsListWidget, *shoppingBasketWidget;
    QComboBox* comboBoxBuy;
    TableModel* tableModel;
    QTableView* shoppingBasketView;

public:
    explicit userGUI(ServiceUser& serviceUser);

    void initGUI();

    void populateCoatsList();

    void populateShoppingBasket();

    void connectSignalsAndSlots();

    int getSelectedIndex();

    void buyCoatOperation();

    void setupPictureTableView();

    void undoOperation();

    void redoOperation();
};

#endif //A89_ALEXTEO24_GUI_H
