#include "lista.h"
#include <iostream>

//10. a. Determine the number formed by adding all even elements and subtracting all odd numbers of the list.
//b. Determine difference of two sets represented as lists.

int numberFormed(PNod list) {
    if (list == nullptr) {
        return 0;
    }
    if (list->e % 2 == 0) {
        return list->e + numberFormed(list->urm);
    }
    if (list->e % 2 == 1) {
        return -list->e + numberFormed(list->urm);
    }
    return 0;
}

bool isInList(PNod l1, TElem elem) {
    if (l1 == nullptr) {
        return false;
    }
    if (l1->e == elem) {
        return true;
    }
    if (l1->e != elem) {
        return isInList(l1->urm, elem);
    }
    return false;
}

PNod difference(PNod l1, PNod l2, PNod l3) {
    if(l1 == nullptr) {
        return l3;
    }
    if(!isInList(l2, l1->e)) {
        if(l3 == nullptr) {
            PNod nod = new Nod();
            nod->e = l1->e;
            l3 = nod;
        } else {
            PNod nod = new Nod();
            nod->e = l1->e;
            PNod last = l3;
            while (last->urm != nullptr) {
                last = last->urm;
            }
            last->urm = nod;
        }
        return difference(l1->urm, l2, l3);
    } else {
        return difference(l1->urm, l2, l3);
    }
}
int main() {
    Lista l;
    std::cout << "Creating list for first requirement\n";
    l = creare();
    std::cout << numberFormed(l._prim) <<'\n';


    Lista l1;
    std::cout << "Creating the first list (A) for the second requirement\n";
    l1 = creare();
    Lista l2;
    std::cout << "Creating the second list(B) for the second requirement\n";
    l2 = creare();
    Lista l3;
    std::cout << "Creating the result list (should be empty) for the second requirement\n";
    l3 = creare();
    l3._prim = difference(l1._prim, l2._prim, l3._prim);
    std::cout << "The difference between the list A and the list B is: ";
    tipar(l3);
//    distruge(l1);
//    distruge(l2);
//    distruge(l3);
    return 0;
}
