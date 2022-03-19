#include "MultiMap.h"
#include "MultiMapIterator.h"
#include <exception>
#include <iostream>

using namespace std;


MultiMap::MultiMap() {
	head = nullptr;
	nrElements = 0;
}
//Time complexity: Theta(1)


void MultiMap::add(TKey c, TValue v) {
	if (nrElements == 0) {
	    Node* newNode = new Node();
	    newNode->info = TElem(c,v);
	    head = newNode;
        nrElements++;
	}
	else {
	    Node* newNode = new Node();
        newNode->info = TElem(c,v);
        newNode->next = head;
        head = newNode;
        nrElements++;
	}
}
//Time complexity: Theta(1)


bool MultiMap::remove(TKey c, TValue v) {
	if (nrElements == 0) {
        return false;
    }
	Node* currentNode;
	currentNode = head;
	if (currentNode->info.first == c && currentNode->info.second == v) {
	    Node* removeHead = head;
	    head = head->next;
	    delete [] removeHead;
	    nrElements--;
        return true;
	}
	Node* previousNode;
	previousNode = currentNode;
	currentNode = currentNode->next;
	while (currentNode != nullptr && currentNode->info != TElem(c, v)) {
	    previousNode = previousNode->next;
	    currentNode = currentNode->next;
	}
	if (currentNode == nullptr) {
        return false;
	}
	else {
	    previousNode->next = currentNode->next;
	    delete [] currentNode;
        nrElements--;
        return true;
	}

}
// Time complexity: Best case: Theta(1), worst case: Theta(n), average case: Theta(n), Total complexity: O(n)


vector<TValue> MultiMap::search(TKey c) const {
	vector<TValue> matching{};
	Node* start = head;
	while (start != nullptr) {
	    if (start->info.first == c) {
	        matching.push_back(start->info.second);
	    }
	    start = start->next;
	}
	return matching;
}
//Time complexity: Theta(n)


int MultiMap::size() const {
    return nrElements;
}
//Time complexity: Theta(1)


bool MultiMap::isEmpty() const {
    return nrElements == 0;
}
//Time complexity: Theta(1)

MultiMapIterator MultiMap::iterator() const {
	return MultiMapIterator(*this);
}
//Time complexity: Theta(1)


MultiMap::~MultiMap() {
	Node* removeHead = nullptr;
	while (head != nullptr) {
	    removeHead = head;
	    head = head->next;
	    delete [] removeHead;
	}
}
//Time complexity: Theta(n)

vector<TValue> MultiMap::removeKey(TKey key) {
    vector<TValue> removed{};
    if (nrElements == 0) {
        return removed;
    }
    Node* currentNode;
    currentNode = head;
    while (currentNode->info.first == key) {
        Node* removeHead = head;
        head = head->next;
        removed.push_back(currentNode->info.second);
        delete [] removeHead;
        currentNode = head;
        nrElements--;
    }
    Node* previousNode;
    previousNode = currentNode;
    currentNode = currentNode->next;
    while (currentNode != nullptr) {
        if (currentNode->info.first == key) {
            previousNode->next = currentNode->next;
            removed.push_back(currentNode->info.second);
            delete[] currentNode;
            currentNode = previousNode->next;
            nrElements--;
        }
        else {
            previousNode = previousNode->next;
            currentNode = currentNode->next;
        }
    }
    return removed;
}
//Time complexity: Theta(n)

MultiMap::Node::Node(): next{nullptr}, info{NULL_TELEM}{}
//Time complexity: Theta(1)