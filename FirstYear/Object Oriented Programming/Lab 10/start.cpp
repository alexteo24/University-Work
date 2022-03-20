//
// Created by Teo on 5/1/2021.
//

#include "GUI.h"
#include <QtWidgets/QApplication>
#include <memory>
#include <QDebug>

int main(int argc, char* argv[]) {
    QApplication a(argc, argv);
    RepositoryCoatsFile repoCoatsFile;
    ServiceAdministrator serviceAdmin{repoCoatsFile};
    std::unique_ptr<RepositoryShopping> repositoryShopping = std::make_unique<HTMLShoppingBasket>();
//    std::unique_ptr<RepositoryShopping> repositoryShopping = std::make_unique<CSVShoppingBasket>();
    ServiceUser serviceUser{repoCoatsFile, repositoryShopping.get()};
    GUI theGui{serviceAdmin, serviceUser};
    theGui.show();
    return a.exec();
}