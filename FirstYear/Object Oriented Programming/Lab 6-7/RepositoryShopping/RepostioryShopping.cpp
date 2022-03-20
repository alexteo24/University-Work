//
// Created by Teo on 4/12/2021.
//

#include <fstream>
#include "RepostioryShopping.h"

RepositoryShopping::RepositoryShopping() : RepositoryCoats() {}

RepositoryShopping::~RepositoryShopping() = default;

void HTMLAdoptionList::write() {
    std::fstream html("../ShoppingCart.html");
    html<<"<!DOCTYPE html>\n"
          "<html>\n"
          "<head>\n"
          "    <title>Shopping cart</title>\n"
          "</head>\n"
          "<body>\n"
          "<table border=\"1\">\n"
          "    <tr> <!-- tr = table row; 1 row for each entity -->\n"
          "        <td>Size</td> <!-- td = table data; 1 td for each attribute of the entity -->\n"
          "        <td>Color</td>\n"
          "        <td>Unique</td>\n"
          "        <td>Price</td>\n"
          "        <td>Quantity</td>\n"
          "        <td>Photograph Link</td>\n"
          "    </tr>\n";
    for (auto const& coat : getVector()) {
        html<<"<tr>\n<td>"<<coat.getSize()<<"</td>\n<td>"<<coat.getColor()<<"<td>\n</td>"<<coat.getUniqueID()<<
        "<td>\n</td>"<<coat.getPrice()<<"<td>\n</td>"<<coat.getQuantity()<<"<td>\n</td><a href=\""
        <<coat.getPhotographLink()<<"\">Link</a></td>\n</tr>\n";}
    html<<"</table>\n"
          "</body>\n"
          "</html>";
    html.close();
}

void HTMLAdoptionList::open() {
    std::string open = "start " + std::string("../ShoppingCart.html");
    system(open.c_str());
}

HTMLAdoptionList::HTMLAdoptionList(): RepositoryShopping(){}

void CSVAdoptionList::write() {
    std::fstream csv("../ShoppingCart.csv");
    if(!csv.is_open()) {
        return;
    }
    for (auto const& i : getVector()) {
        csv<<i<<'\n';
    }
    csv.close();
}

void CSVAdoptionList::open() {
    std::string open = "start " + std::string("../ShoppingCart.csv");
    system(open.c_str());
}

CSVAdoptionList::CSVAdoptionList(): RepositoryShopping() {}
