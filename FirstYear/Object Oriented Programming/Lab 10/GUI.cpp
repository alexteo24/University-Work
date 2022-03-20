//
// Created by Teo on 5/1/2021.
//

#include "GUI.h"

void stringToUpper(std::string &_string) {
    int index;
    for (index = 0; index < _string.length(); index++) {
        if (_string[index] >= 'a' && _string[index] <= 'z') {
            _string[index] -= 32;
        }
    }
}

adminGUI::adminGUI(ServiceAdministrator &serviceAdministrator): _serviceAdministrator{serviceAdministrator} {
    initGUI();
    populateList();
    connectSignalsAndSlots();
}

void adminGUI::initGUI() {
    this->resize(600, 600);
    coatsListWidget = new QListWidget{};
//    coatsTableModel = new CoatsTableModel{_serviceAdministrator.getRepository()};
//    coatsTableView = new QTableView{this};
//    coatsTableView->setModel(coatsTableModel)
    sizeLineEdit = new QLineEdit{};
    colorLineEdit = new QLineEdit{};
    uniqueIDLineEdit = new QLineEdit{};
    photographLinkLineEdit = new QLineEdit{};
    priceLineEdit = new QLineEdit{};
    quantityLineEdit = new QLineEdit{};

    addButton = new QPushButton{"Add"};
    deleteButton = new QPushButton{"Delete"};
    updateButton = new QPushButton{"Update"};
    displayPieChartButton = new QPushButton{"Statistics"};
    undoButton = new QPushButton{"Undo"};
    redoButton = new QPushButton{"Redo"};

    QVBoxLayout* mainLayout = new QVBoxLayout{this};
    mainLayout->addWidget(coatsListWidget);

    QFormLayout* coatDetailsLayout = new QFormLayout{};
    coatDetailsLayout->addRow("Size", sizeLineEdit);
    coatDetailsLayout->addRow("Color", colorLineEdit);
    coatDetailsLayout->addRow("Unique ID", uniqueIDLineEdit);
    coatDetailsLayout->addRow("Photograph Link", photographLinkLineEdit);
    coatDetailsLayout->addRow("Price", priceLineEdit);
    coatDetailsLayout->addRow("Quantity", quantityLineEdit);

    mainLayout->addLayout(coatDetailsLayout);

    QVBoxLayout* buttonsMainLayout = new QVBoxLayout{};
    QHBoxLayout* firstButtonsLayout = new QHBoxLayout{};
    QHBoxLayout* undoRedoLayout = new QHBoxLayout{};
    firstButtonsLayout->addWidget(addButton);
    firstButtonsLayout->addWidget(deleteButton);
    firstButtonsLayout->addWidget(updateButton);
    firstButtonsLayout->addWidget(displayPieChartButton);
    undoRedoLayout->addWidget(undoButton);
    undoRedoLayout->addWidget(redoButton);

    buttonsMainLayout->addLayout(firstButtonsLayout);
    buttonsMainLayout->addLayout(undoRedoLayout);

    mainLayout->addLayout(buttonsMainLayout);

}

void adminGUI::populateList() {
    coatsListWidget->clear();
    std::vector<Coat> coatsList = _serviceAdministrator.getCoatList();
    for(Coat& coat: coatsList) {
        coatsListWidget->addItem(QString::fromStdString(coat.toString()));
    }
}

void adminGUI::connectSignalsAndSlots() {
    QObject::connect(coatsListWidget, &QListWidget::itemClicked, [this](){
        int selected = getSelectedIndex();
        if (selected < 0) {
            return;
        }
        Coat& sCoat = _serviceAdministrator.getCoatList()[selected];
        sizeLineEdit->setText(QString::fromStdString(sCoat.getSize()));
        colorLineEdit->setText(QString::fromStdString(sCoat.getColor()));
        uniqueIDLineEdit->setText(QString::fromStdString(sCoat.getUniqueID()));
        photographLinkLineEdit->setText(QString::fromStdString(sCoat.getPhotographLink()));
        priceLineEdit->setText(QString::fromStdString(std::to_string(sCoat.getPrice())));
        quantityLineEdit->setText(QString::fromStdString(std::to_string(sCoat.getQuantity())));
    });
    QObject::connect(addButton, &QPushButton::clicked, this, &adminGUI::addCoatOperation);
    QObject::connect(deleteButton, &QPushButton::clicked, this, &adminGUI::deleteCoatOperation);
    QObject::connect(updateButton, &QPushButton::clicked, this, &adminGUI::updateCoatOperation);
    QObject::connect(displayPieChartButton, &QPushButton::clicked, this, &adminGUI::displayStatistics);
    QShortcut *undoShortcut = new QShortcut(QKeySequence("Ctrl+Z"), this);
    QShortcut *redoShortcut = new QShortcut(QKeySequence("Ctrl+Y"), this);

    QObject::connect(undoShortcut, &QShortcut::activated, this, &adminGUI::undoOperation);
    QObject::connect(redoShortcut, &QShortcut::activated, this, &adminGUI::redoOperation);
    QObject::connect(undoButton, &QPushButton::clicked, this, &adminGUI::undoOperation);
    QObject::connect(redoButton, &QPushButton::clicked, this, &adminGUI::redoOperation);
}

int adminGUI::getSelectedIndex() {
    auto selectedIndexes = this->coatsListWidget->selectionModel()->selectedIndexes();
    if(selectedIndexes.empty()){
        this->sizeLineEdit->clear();
        this->colorLineEdit->clear();
        this->uniqueIDLineEdit->clear();
        this->photographLinkLineEdit->clear();
        this->priceLineEdit->clear();
        this->quantityLineEdit->clear();
        return -1;
    }

    int selectedIndex = selectedIndexes.at(0).row();
    return selectedIndex;
}

void adminGUI::addCoatOperation() {
    std::string size = sizeLineEdit->text().toStdString();
    stringToUpper(size);
    std::string color = colorLineEdit->text().toStdString();
    stringToUpper(color);
    std::string uniqueID = uniqueIDLineEdit->text().toStdString();
    stringToUpper(uniqueID);
    std::string photographLink = photographLinkLineEdit->text().toStdString();
    if (size.empty() || color.empty() || uniqueID.empty() || photographLink.empty() ||
        priceLineEdit->text().toStdString().empty() || quantityLineEdit->text().toStdString().empty()) {
        QMessageBox::critical(this, "Error", "Please make sure no fields are empty!");
        return;
    }
    int price = std::stoi(priceLineEdit->text().toStdString());
    int quantity = std::stoi(quantityLineEdit->text().toStdString());
    try {
        _serviceAdministrator.addCoatService(size, color, uniqueID, photographLink, price, quantity);
    } catch (ValidationException& validationException) {
        QMessageBox::critical(this, "Error", validationException.what());
        return;
    } catch (RepositoryCoatsException& repositoryCoatsException) {
        QMessageBox::critical(this, "Error", repositoryCoatsException.what());
        return;
    }
    populateList();

    coatsListWidget->setCurrentRow(_serviceAdministrator.getCoatList().size() - 1);
    QMessageBox::about(this, "Success", "Addition was successful!");

}

void adminGUI::deleteCoatOperation() {
    int selected = getSelectedIndex();
    if (selected < 0) {
        QMessageBox::critical(this, "Error", "No coat selected for deletion!");
        return;
    }
    std::string coatID = uniqueIDLineEdit->text().toStdString();
    try {
        _serviceAdministrator.deleteCoatService(coatID);
    } catch (RepositoryCoatsException& repositoryCoatsException) {
        QMessageBox::critical(this, "Error", repositoryCoatsException.what());
        return;
    }
    populateList();

    coatsListWidget->setCurrentRow(_serviceAdministrator.getCoatList().size() - 1);
    QMessageBox::about(this, "Success", "Deletion was successful!");
}

void adminGUI::updateCoatOperation() {
    std::string size = sizeLineEdit->text().toStdString();
    stringToUpper(size);
    std::string color = colorLineEdit->text().toStdString();
    stringToUpper(color);
    std::string uniqueID = uniqueIDLineEdit->text().toStdString();
    stringToUpper(uniqueID);
    std::string photographLink = photographLinkLineEdit->text().toStdString();
    if (size.empty() || color.empty() || uniqueID.empty() || photographLink.empty() ||
            priceLineEdit->text().toStdString().empty() || quantityLineEdit->text().toStdString().empty()) {
        QMessageBox::critical(this, "Error", "Please make sure no fields are empty!");
        return;
    }
    int price = std::stoi(priceLineEdit->text().toStdString());
    int quantity = std::stoi(quantityLineEdit->text().toStdString());
    try {
        _serviceAdministrator.updateCoatService(size, color, uniqueID, photographLink, price, quantity);
    } catch (ValidationException& validationException) {
        QMessageBox::critical(this, "Error", validationException.what());
        return;
    } catch (RepositoryCoatsException& repositoryCoatsException) {
        QMessageBox::critical(this, "Error", repositoryCoatsException.what());
        return;
    }
    populateList();
    QMessageBox::about(this, "Success", "Update was successful!");
}

void adminGUI::displayStatistics() {
    QWidget* statisticsWidget = new QWidget{};
    statisticsWidget->setFixedSize(600, 600);
    QVBoxLayout* someLayout = new QVBoxLayout{statisticsWidget};
    QtCharts::QPieSeries *series = new QtCharts::QPieSeries{statisticsWidget};
    std::string sizes[6] = {"S", "M", "L", "XL", "XXL", "XXXL"};
    int i;
    int max = -1;
    int index = -1;
    for(i = 0; i < 6; i++) {
        int amount = _serviceAdministrator.amountOnSize(sizes[i]);
        series->append(QString::fromStdString(sizes[i]), amount);
        if (amount > max) {
            max = amount;
            index = i;
        }
    }

    QtCharts::QPieSlice *slice = series->slices().at(index);
    slice->setExploded();
    slice->setLabelVisible();
    slice->setPen(QPen(Qt::darkGreen, 2));
    slice->setBrush(Qt::green);

    QtCharts::QChart *chart = new QtCharts::QChart{};
    chart->addSeries(series);
    chart->setTitle("Size statistics");

    QtCharts::QChartView *chartView = new QtCharts::QChartView(chart);
    chartView->setRenderHint(QPainter::Antialiasing);
    someLayout->addWidget(chartView);
    statisticsWidget->show();
}

void adminGUI::undoOperation() {
    try {
        _serviceAdministrator.undo();
        this->sizeLineEdit->clear();
        this->colorLineEdit->clear();
        this->uniqueIDLineEdit->clear();
        this->photographLinkLineEdit->clear();
        this->priceLineEdit->clear();
        this->quantityLineEdit->clear();
        populateList();
    } catch (RepositoryCoatsException& repositoryCoatsException) {
        QMessageBox::information(this, "Error", repositoryCoatsException.what());
        return;
    }
}

void adminGUI::redoOperation() {
    try {
        _serviceAdministrator.redo();
        this->sizeLineEdit->clear();
        this->colorLineEdit->clear();
        this->uniqueIDLineEdit->clear();
        this->photographLinkLineEdit->clear();
        this->priceLineEdit->clear();
        this->quantityLineEdit->clear();
        populateList();
    } catch (RepositoryCoatsException& repositoryCoatsException) {
        QMessageBox::information(this, "Error", repositoryCoatsException.what());
        return;
    }
}

userGUI::userGUI(ServiceUser& serviceUser): _serviceUser{serviceUser} {
    initGUI();
    populateCoatsList();
    populateShoppingBasket();
    connectSignalsAndSlots();
}

void userGUI::initGUI() {
    QVBoxLayout* mainLayout = new QVBoxLayout{this};

    QHBoxLayout* labelsLayout = new QHBoxLayout{};
    coatsListLabel = new QLabel{"Available coats for you:"};
    shoppingBasketLabel = new QLabel{"Your shopping cart:"};
    labelsLayout->addWidget(coatsListLabel);
    labelsLayout->addWidget(shoppingBasketLabel);
    mainLayout->addLayout(labelsLayout);

    QHBoxLayout* listWidgetLayout = new QHBoxLayout{};
    coatsListWidget = new QListWidget{};
//    shoppingBasketWidget = new QListWidget{};
    shoppingBasketView = new QTableView{};
    tableModel = new TableModel{_serviceUser};
    shoppingBasketView->setModel(tableModel);
    totalCost = new QLabel{"Total cost: "};
    QVBoxLayout* shopElementsLayout = new QVBoxLayout{};
//    shopElementsLayout->addWidget(shoppingBasketWidget);
    setupPictureTableView();
    shopElementsLayout->addWidget(shoppingBasketView);
    shopElementsLayout->addWidget(totalCost);
    listWidgetLayout->addWidget(coatsListWidget);
    listWidgetLayout->addLayout(shopElementsLayout);
    mainLayout->addLayout(listWidgetLayout);

    QFormLayout* lineEditsLayout = new QFormLayout{};
    coatSizeLineEdit = new QLineEdit{};
    lineEditsLayout->addRow("Size", coatSizeLineEdit);
    coatColorLineEdit = new QLineEdit{};
    lineEditsLayout->addRow("Color", coatColorLineEdit);
    coatPriceLineEdit = new QLineEdit{};
    lineEditsLayout->addRow("Price", coatPriceLineEdit);
    mainLayout->addLayout(lineEditsLayout);

    QHBoxLayout* filterLayout = new QHBoxLayout{};
    filterCoatsButton = new QPushButton{"Filter"};
    filterSizeLineEdit = new QLineEdit{};
    filterLayout->addWidget(filterCoatsButton);
    filterLayout->addWidget(filterSizeLineEdit);
    mainLayout->addLayout(filterLayout);

    QVBoxLayout* buttonsMainLayout = new QVBoxLayout{};
    QHBoxLayout* buttonsLayout = new QHBoxLayout{};
    addCoatButton = new QPushButton{"Add to cart"};
    openShoppingBasketButton = new QPushButton{"Open file"};
    comboBoxBuy = new QComboBox{};
    checkoutButton = new QPushButton{"Checkout"};
    comboBoxBuy->setFixedSize(50, 25);
    buttonsLayout->addWidget(addCoatButton);
    buttonsLayout->addWidget(comboBoxBuy);
    buttonsLayout->addWidget(checkoutButton);
    buttonsLayout->addWidget(openShoppingBasketButton);

    QHBoxLayout* undoRedoLayout = new QHBoxLayout{};
    undoButton = new QPushButton{"Undo"};
    redoButton = new QPushButton{"Redo"};
    undoRedoLayout->addWidget(undoButton);
    undoRedoLayout->addWidget(redoButton);

    buttonsMainLayout->addLayout(buttonsLayout);
    buttonsMainLayout->addLayout(undoRedoLayout);

    mainLayout->addLayout(buttonsMainLayout);


}

void userGUI::populateCoatsList() {
    coatsListWidget->clear();
    for(Coat& sCoat:_serviceUser.getMatchingList()) {
        if(sCoat.getQuantity() != 0) {
            coatsListWidget->addItem(QString::fromStdString("Size: " + sCoat.getSize() +
            ", " + "Color: " + sCoat.getColor() + ", " + "Price: " + std::to_string(sCoat.getPrice())));
        }
    }
}

void userGUI::populateShoppingBasket() {
    shoppingBasketView->setModel(nullptr);
    shoppingBasketView->setModel(tableModel);
    shoppingBasketView->resizeColumnsToContents();
}

void userGUI::connectSignalsAndSlots() {
    QObject::connect(coatsListWidget, &QListWidget::itemClicked, [this](){
        int selected = getSelectedIndex();
        if (selected < 0) {
            return;
        }
        Coat& sCoat = _serviceUser.getCoatList()[selected];
        coatSizeLineEdit->setText(QString::fromStdString(sCoat.getSize()));
        coatColorLineEdit->setText(QString::fromStdString(sCoat.getColor()));
        coatPriceLineEdit->setText(QString::fromStdString(std::to_string(sCoat.getPrice())));
        int i;
        comboBoxBuy->clear();
        for (i = 1; i < sCoat.getQuantity() + 1; i++) {
            comboBoxBuy->addItem(QString::fromStdString(std::to_string(i)));
        }
        comboBoxBuy->setCurrentIndex(0);
    });
    QObject::connect(addCoatButton, &QPushButton::clicked, this, &userGUI::buyCoatOperation);
    QObject::connect(filterCoatsButton, &QPushButton::clicked, [this](){
        std::string size = filterSizeLineEdit->text().toStdString();
        stringToUpper(size);
        _serviceUser.findMatchingSize(size);
        if (_serviceUser.anyMatchingCoats()) {
            populateCoatsList();
            QMessageBox::about(this, "Filtering done", "There are no coats having the desired size!");
            return ;
        } else {
            populateCoatsList();
        }
    });
    QObject::connect(openShoppingBasketButton, &QPushButton::clicked, [this](){_serviceUser.write();_serviceUser.open();});
    QObject::connect(checkoutButton, &QPushButton::clicked, [this](){_serviceUser.checkOut();});

    QShortcut *undoShortcut = new QShortcut(QKeySequence("Ctrl+Z"), this);
    QShortcut *redoShortcut = new QShortcut(QKeySequence("Ctrl+Y"), this);

    QObject::connect(undoShortcut, &QShortcut::activated, this, &userGUI::undoOperation);
    QObject::connect(redoShortcut, &QShortcut::activated, this, &userGUI::redoOperation);
    QObject::connect(undoButton, &QPushButton::clicked, this, &userGUI::undoOperation);
    QObject::connect(redoButton, &QPushButton::clicked, this, &userGUI::redoOperation);
}

int userGUI::getSelectedIndex() {
    auto selectedIndexes = this->coatsListWidget->selectionModel()->selectedIndexes();
    if(selectedIndexes.empty()){
        this->coatSizeLineEdit->clear();
        this->coatColorLineEdit->clear();
        this->coatPriceLineEdit->clear();
        return -1;
    }

    int selectedIndex = selectedIndexes.at(0).row();
    return selectedIndex;
}

void userGUI::buyCoatOperation() {
    int currentIndex = getSelectedIndex();

    if (currentIndex < 0) {
        QMessageBox::critical(this, "Error", "No coat selected to purchase!");
        return;
    } else {
        try {
            Coat& currentCoat = _serviceUser.getMatchingList()[currentIndex];
            int amount = comboBoxBuy->currentIndex() + 1;
            _serviceUser.addToCart(currentCoat, amount);
            totalCost->setText(QString::fromStdString("Total cost: "+ std::to_string(_serviceUser.computeCost())));
        } catch (ValidationException& validationException) {
            QMessageBox::critical(this, "Error", validationException.what());
            return;
        } catch (RepositoryCoatsException& repositoryCoatsException) {
            QMessageBox::critical(this, "Error", repositoryCoatsException.what());
            return;
        } catch (ShoppingException& shoppingException) {
            QMessageBox::critical(this, "Error", shoppingException.what());
            return;
        }
        populateCoatsList();
        populateShoppingBasket();

        coatsListWidget->setCurrentRow(currentIndex);
        QMessageBox::about(this, "Success", "Addition was successful!");
    }

}

void userGUI::undoOperation() {
    try {
        _serviceUser.undo();
        populateShoppingBasket();
        totalCost->setText(QString::fromStdString("Total cost: "+ std::to_string(_serviceUser.computeCost())));
    } catch (ShoppingException& shoppingException) {
        QMessageBox::information(this, "Error", shoppingException.what());
        return;
    } catch (RepositoryCoatsException& repositoryCoatsException) {
        QMessageBox::information(this, "Error", repositoryCoatsException.what());
        return;
    }
}

void userGUI::redoOperation() {
    try {
        _serviceUser.redo();
        populateShoppingBasket();
        totalCost->setText(QString::fromStdString("Total cost: "+ std::to_string(_serviceUser.computeCost())));
    } catch (ShoppingException& shoppingException) {
        QMessageBox::information(this, "Error", shoppingException.what());
        return;
    } catch (RepositoryCoatsException& repositoryCoatsException) {
        QMessageBox::information(this, "Error", repositoryCoatsException.what());
        return;
    }
}

void userGUI::setupPictureTableView() {
    shoppingBasketView->setModel(tableModel);
    shoppingBasketView->setItemDelegate(new PictureDelegate{});
    shoppingBasketView->resizeColumnsToContents();
    shoppingBasketView->resizeRowsToContents();
}

GUI::GUI(ServiceAdministrator& serviceAdministrator, ServiceUser& serviceUser):_serviceAdministrator{serviceAdministrator},
                                                                                _serviceUser{serviceUser} {
    initGUI();
}

void GUI::initGUI() {
    QVBoxLayout* theLayout = new QVBoxLayout{this};
    QLabel* someLabel = new QLabel{"Welcome to the shop!"};
    QFont someLabelFont {};
    someLabelFont.setPixelSize(20);
    someLabelFont.setBold(true);
    someLabel->setFont(someLabelFont);
    theLayout->addWidget(someLabel);

    QHBoxLayout* buttonsLayout = new QHBoxLayout{};
    QPushButton* adminButton = new QPushButton{"Admin"};
    QPushButton* userButton = new QPushButton{"User"};
    buttonsLayout->addWidget(adminButton);
    buttonsLayout->addWidget(userButton);
    theLayout->addLayout(buttonsLayout);
    QObject::connect(adminButton, &QPushButton::clicked, [this](){
        hide();
        adminGUI* adminGui = new adminGUI{_serviceAdministrator};
        adminGui->show();
    });
    QObject::connect(userButton, &QPushButton::clicked, [this](){
        hide();
        userGUI* userGui = new userGUI{_serviceUser};
        userGui->show();
    });
}