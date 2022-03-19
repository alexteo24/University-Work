#include "ListIterator.h"
#include "IteratedList.h"
#include <exception>

ListIterator::ListIterator(IteratedList& list) : list(list) {
	currentNode = list.head;
}//Time complexity: Theta(1)

void ListIterator::first() {
    currentNode = list.head;
}//Time complexity: Theta(1)

void ListIterator::next() {
	if (!valid()) {
	    throw std::exception();
	} else {
	    currentNode = list.nodes[currentNode].next;
	}
}//Time complexity: Theta(1)

bool ListIterator::valid() const {
	if (currentNode == -1) {
        return false;
	}
    return true;
}//Time complexity: Theta(1)

TElem ListIterator::getCurrent() const {
	if (!valid()) {
        throw std::exception();
	} else {
        return list.nodes[currentNode].info;
	}
}//Time complexity: Theta(1)

TElem ListIterator::remove() {
    if (!valid()) {
        throw std::exception();
    }
    TElem removedValue;
    int currNode = currentNode;
    removedValue = getCurrent();
    currentNode = list.nodes[currNode].next;
    if (currNode == list.head) {
        list.nrElements--;
        if (list.nrElements == 0) {
            list.tail = -1;
            list.head = -1;
            list.nodes[currNode].next = list.firstEmpty;
            list.firstEmpty = currNode;
        } else {
            list.head = list.nodes[currNode].next;
            list.nodes[list.head].prev = -1;
            list.nodes[currNode].next = list.firstEmpty;
            list.firstEmpty = currNode;
        }
    } else if (currNode == list.tail) {
        list.tail = list.nodes[currNode].prev;
        list.nodes[list.tail].next = -1;
        list.nodes[currNode].next = list.firstEmpty;
        list.firstEmpty = currNode;
        list.nrElements--;
    } else {
        list.nodes[list.nodes[currNode].prev].next = list.nodes[currNode].next;
        list.nodes[list.nodes[currNode].next].prev = list.nodes[currNode].prev;
        list.nrElements--;
        list.nodes[currNode].next = list.firstEmpty;
        list.firstEmpty = currNode;
    }
    return removedValue;
}//Time complexity: Theta(1)
