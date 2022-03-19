#include "Matrix.h"
#include <exception>
using namespace std;

Matrix::Matrix(int nrLines, int nrCols) {
    noLines = nrLines;
    noColumns = nrCols;
    nrElements = 0;
    capacity = 10;
    hashtable = new Node*[capacity]();
}// Time complexity: Theta(1)


int Matrix::nrLines() const {
    return noLines;
}// Time complexity: Theta(1)


int Matrix::nrColumns() const {
    return noColumns;
}// Time complexity: Theta(1)


TElem Matrix::element(int i, int j) const {
    if (i < 0 || j < 0 || i > noLines - 1 || j > noColumns - 1) {
        throw std::exception();
    }
	int index = (i * noColumns + j) % capacity;
    Node* currentNode = hashtable[index];
    while (currentNode != nullptr) {
        if (currentNode->row == i && currentNode->column == j) {
            return currentNode->info;
        }
        if (currentNode->row > i || currentNode->row == i && currentNode->column > j) {
            return NULL_TELEM;
        }
        currentNode = currentNode->next;
    }
    return NULL_TELEM;
}//Time complexity: Best case: Theta(1), Average Case: (1 + load factor), Worst case: O(n)

TElem Matrix::modify(int i, int j, TElem e) {
    if (i < 0 || j < 0 || i > noLines - 1 || j > noColumns - 1) {
        throw std::exception();
    }
	int index = (i * noColumns + j) % capacity;
	TElem oldValue = NULL_TELEM;
	Node* currentNode = hashtable[index];
	if (currentNode == nullptr) { // no element at the current index
	    currentNode = new Node;
	    hashtable[index] = currentNode;
	    currentNode->row = i;
        currentNode->column = j;
        currentNode->info = e;
        nrElements++;
    } else { // at least 1 element
	    bool isFirst = true;
	    Node* previousNode = currentNode;
	    while(currentNode != nullptr) {
	        if(currentNode->row > i || currentNode->row == i && currentNode->column >= j) {
                break;
	        }
	        isFirst = false;
	        previousNode = currentNode;
	        currentNode = currentNode->next;
	    }
	    if(e != NULL_TELEM) { // if we actually want to add an element\modify without deleting
	        if (currentNode != nullptr) { // if we didn't get to the end
                if (currentNode->row == i && currentNode->column == j) { // if the element already exists
                    oldValue = currentNode->info;
                    currentNode->info = e;
                } else if (isFirst) { // stopped at current and must insert either before or after
                    nrElements++;
                    Node *newNode = new Node;
                    newNode->row = i;
                    newNode->column = j;
                    newNode->info = e;
                    if (i < currentNode->row || i == currentNode->row && j < currentNode->column){ // before
                        newNode->next = currentNode;
                        hashtable[index] = newNode;
                    }
                } else { // not the first one, so we can use previous, inserts before
                    nrElements++;
                    Node *newNode = new Node;
                    newNode->row = i;
                    newNode->column = j;
                    newNode->info = e;
                    newNode->next = previousNode->next;
                    previousNode->next = newNode;
                }
            } else { // if the new element should be the last
                nrElements++;
                Node *newNode = new Node;
                newNode->row = i;
                newNode->column = j;
                newNode->info = e;
                newNode->next = currentNode;
                previousNode->next = newNode;
	        }
        } else {
	        if (currentNode != nullptr) { // if the element exists and we must delete it
                if (currentNode->row == i && currentNode->column == j) { // only if it exists we delete
                    if (isFirst) { // The first one has to get eliminated, but must take care if it is the only elem
                        if (currentNode->next == nullptr) { // it is the only element
                            oldValue = currentNode->info;
                            nrElements--;
                            delete [] currentNode;
                            hashtable[index] = nullptr;
                        } else { // it is not the only element
                            oldValue = currentNode->info;
                            hashtable[index] = currentNode->next;
                            nrElements--;
                            delete [] currentNode;
                        }
                    } else { // it is not the only one, so we can use the previous
                        oldValue = currentNode->info;
                        previousNode->next = currentNode->next;
                        nrElements--;
                        delete [] currentNode;
                    }
                }
            }
	    }
	}
    if (nrElements * 10 / capacity >= 7) {
        resizeAndRehash();
    }
    return oldValue;
}// Time complexity: Best case: Theta(1) amortized, Average Case: (1 + load factor), Worst case: O(n)

void Matrix::resizeAndRehash() {
    Node** newHashTable = new Node*[capacity * 2]();
    int i;
    int index;
    for(i = 0; i < capacity; i++) {
        Node* currentNode = hashtable[i];
        while (currentNode != nullptr) {
            index = (currentNode->row * noColumns + currentNode->column) % (capacity * 2);
            if (newHashTable[index] == nullptr) {
                newHashTable[index] = new Node;
                newHashTable[index]->row = currentNode->row;
                newHashTable[index]->column = currentNode->column;
                newHashTable[index]->info = currentNode->info;
            } else {
                bool isFirst = true;
                Node* actualNode = newHashTable[index];
                Node* previousNode = actualNode;
                while(actualNode != nullptr) {
                    if(actualNode->row > currentNode->row || actualNode->row == currentNode->row && actualNode->column >= currentNode->column) {
                        break;
                    }
                    isFirst = false;
                    previousNode = actualNode;
                    actualNode = actualNode->next;
                }
                if (actualNode != nullptr) { // if we didn't get to the end
                        if (isFirst) { // stopped at current and must insert either before or after
                            Node *newNode = new Node;
                            newNode->row = currentNode->row;
                            newNode->column = currentNode->column;
                            newNode->info = currentNode->info;
                        if (currentNode->row < actualNode->row || currentNode->row == actualNode->row && currentNode->column < actualNode->column){ // before
                            newNode->next = actualNode;
                            hashtable[index] = newNode;
                        }
                    } else { // not the first one, so we can use previous, inserts before
                        Node *newNode = new Node;
                        newNode->row = currentNode->row;
                        newNode->column = currentNode->column;
                        newNode->info = currentNode->info;
                        newNode->next = previousNode->next;
                        previousNode->next = newNode;
                    }
                } else { // if the new element should be the last
                    Node *newNode = new Node;
                    newNode->row = currentNode->row;
                    newNode->column = currentNode->column;
                    newNode->info = currentNode->info;
                    newNode->next = previousNode->next;
                    previousNode->next = newNode;
                }
            }
            Node* deletionNode = currentNode;
            currentNode = currentNode->next;
            delete[] deletionNode;

        }
    }
    delete [] hashtable;
    capacity *= 2;
    hashtable = newHashTable;
} //Time complexity: Theta(n + m), where n is the capacity and m is the number of elements

Matrix::~Matrix() {
    int i;
    Node* removeNode;
    Node* currentNode;
    for(i = 0; i < capacity; i++) {
        currentNode = hashtable[i];
        while(currentNode != nullptr) {
            removeNode = currentNode;
            currentNode = currentNode->next;
            delete [] removeNode;
        }
    }
    delete [] hashtable;
}//Time complexity: Theta(n + m), where n is the capacity and m is the number of elements

void Matrix::resize(int newLines, int newCol) {
    if (newLines <= 0 || newCol <= 0) {
        throw std::exception();
    }
    if (newLines < noLines || newCol < noColumns) { // elements should start getting removed
        int i;
        for (i = 0; i < capacity; i++) {
            Node* currentNode = hashtable[i];
            bool anyNodesLeft = false;
            Node* headReplace = hashtable[i];
            Node* previousNode = nullptr;
            while (currentNode != nullptr) {
                if (currentNode->row >= newLines || currentNode->column >= newCol) { // it wouldn't fit
                    if (currentNode == headReplace) {
                        headReplace = currentNode->next;
                    }
                    if (anyNodesLeft) {
                        previousNode->next = currentNode->next;
                    }
                    nrElements--;
                    Node* deleteNode = currentNode;
                    currentNode = currentNode->next;
                    delete [] deleteNode;
                } else {
                    anyNodesLeft = true;
                    previousNode = currentNode;
                    currentNode = currentNode->next;
                }
            }
            hashtable[i] = headReplace;
        }
    }
    noLines = newLines;
    noColumns = newCol;
}//Time complexity: Theta(n + m), where n is the capacity and m is the number of elements


