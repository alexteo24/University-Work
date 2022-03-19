
#include <exception>
#include "ListIterator.h"
#include "IteratedList.h"
#include <iostream>

IteratedList::IteratedList() {
	//TODO - Implementation
	nrElements = 0;
	capacity = 10;
	nodes = new DLLANode[capacity];
	head = -1;
	tail = -1;
	firstEmpty = 0;
	int i;
	for (i = 0; i < capacity - 1; i++) {
        nodes[i].next = i + 1;
	}
	nodes[capacity - 1].next = -1;
}//Time complexity: Theta(n)

int IteratedList::size() const {
    return nrElements;
}//Time complexity: Theta(1)

bool IteratedList::isEmpty() const {
    return nrElements == 0;
}//Time complexity: Theta(1)

ListIterator IteratedList::first() {
	return ListIterator(*this);
}//Time complexity: Theta(1)

TElem IteratedList::getElement(ListIterator pos) const {
	if (!pos.valid()) {
	    throw std::exception();
	} else {
        return pos.getCurrent();
	}
}//Time complexity: Theta(1)

TElem IteratedList::remove(ListIterator& pos) {
    if (!pos.valid()) {
        throw std::exception();
    }
    int currentNode = pos.currentNode;
    int removedValue = pos.getCurrent();
    nrElements--;
    if (currentNode == head) {
        if (nrElements == 0) {
            tail = -1;
            head = -1;
            nodes[currentNode].next = firstEmpty;
            firstEmpty = currentNode;
        } else {
            head = nodes[currentNode].next;
            nodes[head].prev = -1;
            nodes[currentNode].next = firstEmpty;
            firstEmpty = currentNode;
        }
        return removedValue;
    } else if (currentNode == tail) {
        tail = nodes[currentNode].prev;
        nodes[tail].next = -1;
        nodes[currentNode].next = firstEmpty;
        firstEmpty = currentNode;
        return removedValue;
    } else {
        nodes[nodes[currentNode].prev].next = nodes[currentNode].next;
        nodes[nodes[currentNode].next].prev = nodes[currentNode].prev;
        nodes[currentNode].next = firstEmpty;
        firstEmpty = currentNode;
        return removedValue;
    }
}//Time complexity: Theta(1)

ListIterator IteratedList::search(TElem e) {
	ListIterator it = first();
	while (it.valid() && it.getCurrent() != e) {
	    it.next();
	}
	return it;
}//Time complexity: Best case Theta(1), worst case Theta(n), average case Theta(n), Total complexity: O(n)

TElem IteratedList::setElement(ListIterator pos, TElem e) {
    if (!pos.valid()) {
        throw std::exception();
    } else {
        TElem old = pos.getCurrent();
        nodes[pos.currentNode].info = e;
        return old;
    }
}//Time complexity: Theta(1)

void IteratedList::addToPosition(ListIterator& pos, TElem e) {
    if (!pos.valid()) {
        throw std::exception();
    }
    if (nrElements == capacity) {
        resize();
    }
    nrElements++;
    int currentNode = firstEmpty;
    firstEmpty = nodes[firstEmpty].next;
    if (pos.currentNode == head) {
        nodes[currentNode].prev = head;
        nodes[currentNode].next = nodes[head].next;
        if (tail == head) {
            tail = currentNode;
        } else {
            nodes[nodes[head].next].prev = currentNode;
        }
        nodes[head].next = currentNode;
        nodes[currentNode].info = e;
        pos.next();
    } else if (pos.currentNode == tail) {
        nodes[tail].next = currentNode;
        nodes[currentNode].prev = tail;
        nodes[currentNode].next = -1;
        nodes[currentNode].info = e;
        tail = currentNode;
        pos.next();
    } else {
        nodes[currentNode].prev = pos.currentNode;
        nodes[currentNode].next = nodes[pos.currentNode].next;
        nodes[nodes[currentNode].next].prev = currentNode;
        nodes[currentNode].info = e;
        nodes[pos.currentNode].next = currentNode;
        pos.next();
    }
}//Time complexity: Theta(1) amortized

void IteratedList::addToBeginning(TElem e) {
    if (nrElements == capacity) {
        resize();
    }
    nrElements++;
    int newNode = firstEmpty;
    firstEmpty = nodes[firstEmpty].next;
    if (head == -1) {
        head = newNode;
        tail = newNode;
        nodes[head].info = e;
        nodes[head].next = -1;
        nodes[head].prev = -1;
    } else {
        nodes[newNode].next = head;
        nodes[newNode].prev = nodes[head].prev;
        nodes[head].prev = newNode;
        nodes[newNode].info = e;
        head = newNode;
    }
}//Time complexity: Theta(1) amortized

void IteratedList::addToEnd(TElem e) {
    int nextEmpty;
    if (capacity == nrElements) {
        resize();
    }
    int newNode = firstEmpty;
    firstEmpty = nodes[firstEmpty].next;
    nrElements++;
    if (tail == -1) {
        nodes[newNode].info = e;
        nodes[newNode].next = -1;
        head = newNode;
        tail = newNode;
    } else {
	    nodes[tail].next = newNode;
	    nodes[newNode].prev = tail;
	    nodes[newNode].info = e;
	    nodes[newNode].next = -1;
	    tail = newNode;
	}
}//Time complexity: Theta(1) amortized

IteratedList::~IteratedList() {
	delete [] nodes;
}//Time complexity: Theta(1)

void IteratedList::resize() {
    DLLANode* newNodes = new DLLANode[capacity * 2];
    int index;
    for(index = 0; index < capacity; index++) {
        newNodes[index] = nodes[index];
    }
    for(index = capacity; index < capacity * 2 - 1; index++) {
        newNodes[index].next = index + 1;
    }
    firstEmpty = capacity;
    capacity *= 2;
    newNodes[capacity - 1].next = -1;
    delete [] nodes;
    nodes = newNodes;
}//Time complexity: Theta(2n) -> Theta(n); where n is the initial capacity