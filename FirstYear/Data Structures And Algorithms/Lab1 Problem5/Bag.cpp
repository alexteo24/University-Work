#include "Bag.h"
#include "BagIterator.h"
#include <exception>
#include <iostream>
using namespace std;


Bag::Bag() {
	this->nrElements = 0;
	this->maxElement = NULL_TELEM;
	this->minElement = -NULL_TELEM;
	this->frequencyCap = 10;
	this->frequency = new int [this->frequencyCap]();
	this->frequencyLength = 0;
	this->previousMin = 0;
	this->previousMax = 0;
}


void Bag::add(TElem elem) {
    bool resizeReq = false;
    bool shiftReq = false;
    if (this->nrElements == 0)  //if there are no elements, we set the min and max to the current elem
    {
        this->minElement = elem;
        this->maxElement = elem;
    }
    if (elem > this->maxElement) {  //we must save the current maximum, and the current max will be our current elem
        this->previousMax = this->maxElement;
        this->maxElement = elem;
    }
    if (elem < this->minElement) {  //we must save the current minimum, the current min will be out current elem
        this->previousMin = this->minElement;
        this->minElement = elem;
        if (this->maxElement - this->minElement + 1 > this->frequencyCap) {  //checking if the new element would fit in our array
            resizeReq = true;
            shiftReq = true;
        }
        else  // it fits
        {
            shiftReq = true;
        }
    }
    if (this->maxElement - this->minElement + 1 > this->frequencyCap) {  // the array isn't large enough to contain all the
        // elements from this->maxElement o this->minElement, so a resize will be required
        resizeReq = true;
    }
    if (resizeReq) {
        this->frequencyCap = (this->maxElement - this->minElement + 1) * 3; // it is way better to determine the new length
        // of the array based on our max and min, other than doubling the array, because sometimes even 5 doubles wouldn't
        // be enough to cover the new element as well
        int * newArray = new int [this->frequencyCap]();
        int index;
        for (index = 0; index < this->frequencyLength; index++) { // moving the current elements and frequencies to the new array
            newArray[index] = this->frequency[index];
        }
        delete [] this->frequency;
        this->frequency = newArray;
    }
    this->frequencyLength = this->maxElement - this->minElement + 1;  // updating the length of the array
    if (shiftReq) {  // if there is a new min element, but there was no room to prepare for its addition, we will make room now
        this->shiftElementsRight();
    }
    int index = elem - this->minElement;
    // adding the new element
    this->nrElements++;
    this->frequency[index]++;
}//Time complexity: BestCase Theta(1) amortized, WorstCase Theta(n), AverageCase Theta(n), Total complexity: O(n)



bool Bag::remove(TElem elem) {
    if (elem < this->minElement or elem > this->maxElement or this->frequency[elem - this->minElement] == 0)
        // if the element is outside the current scope( less than min or greater than max) or its frequency is 0, the
        // removal is not possible
        return false;
    if ((elem != this->minElement and elem != this->maxElement) or (elem == this->maxElement and
    this->frequency[elem - this->minElement] > 1) or (elem == this->minElement and this->frequency[0] > 1)) {
        // if the element is not the min or max, or, if it is one of those but its frequency is > 1, we just remove
        // the element
        this->frequency[elem - this->minElement]--;
        this->nrElements--;
        return true;
    } else if (elem == this->maxElement) {
        // if the element is the max and it appears only once
        this->previousMax = this->getNewPreviousMax();  // get prev max, because in case of an addition of elements in
        // a decreasing order, the previous max will be = 0 (the default value)
        this->frequency[elem - this->minElement]--;  // removing the element
        this->nrElements--;
        this->maxElement = this->previousMax;  // updating the max, since max helps with going through the array
        this->frequencyLength = this->maxElement - this->minElement + 1;  //updating the length, since the length
        // is used to go through the array : i=0,length-1
        return true;
    } else if (elem == this->minElement) {
        // if the element is the min and i appears only once
        this->previousMin = this->getNewPreviousMin(); // get the prev min, because in case of an addition of elements in
        // a increasing order, the previous min will be = 0 (the default value)
        this->shiftElementsLeft();  // shift the array prevMin - min positions to the left, so that we eliminate all
        // the elements between [min, prevMin)
        this->nrElements--;
        this->minElement = this->previousMin;
        this->frequencyLength = this->maxElement - this->minElement + 1;  //updating the length, since the length
        // is used to go through the array : i=0,length-1
        return true;
    }
    return false;
}//Time complexity: BestCase Theta(1), WorstCase Theta(n), AverageCase Theta(n), Total complexity: O(n)


bool Bag::search(TElem elem) const {
    if (elem < this->minElement or elem > this->maxElement)  // if the element is outside the current
        // scope( less than min or greater than max)
        return false;
    if (this->frequency[elem - this->minElement] == 0)  // if it is in [mix, max] but its frequency its 0
        return false;
    return true;
}
//Time complexity: Theta(1)

int Bag::nrOccurrences(TElem elem) const {
	if (elem < this->minElement or elem > this->maxElement)  // if the element is outside the current
	    // scope( less than min or greater than max)
        return 0;
    return this->frequency[elem - this->minElement];
}
//Time complexity: Theta(1)


int Bag::size() const {
    return this->nrElements;
}
//Time complexity: Theta(1)


bool Bag::isEmpty() const {
    return (this->nrElements == 0);
}
//Time complexity: Theta(1)

BagIterator Bag::iterator() const {
	return BagIterator(*this);
}


Bag::~Bag() {
	delete [] this->frequency;
}
//Time complexity: Theta(1) ?

void Bag::shiftElementsRight() {
    int displacement = this->previousMin - this->minElement;
    int index;
    for (index = frequencyLength; index >= 0; index--) {
        this->frequency[index + displacement] = this->frequency[index];  // shifting a number of position
        this->frequency[index] = 0;  // setting 0 on the position we moved from
    }
}//Time complexity: Theta(n) where n = frequencyLength

void Bag::shiftElementsLeft() {
    int displacement = this->previousMin - this->minElement;
    int index;
    for (index = 0; index < this->frequencyLength; index++) {
        this->frequency[index] = this->frequency[index + displacement];  // shifting a number of position
        this->frequency[index + displacement] = 0;  // setting 0 on the position we moved from
    }
}//Time complexity: Theta(n) where n = frequencyLength

int Bag::getNewPreviousMin() {
    int index;
    for (index = 1; index < frequencyLength - 1; index ++){
        if (this->frequency[index] != 0) {  // we found a position, different from the one on which the actual min is
            int newPrevMin = index + this->minElement;
            return newPrevMin;  // returning the prev min
        }
    }
    return this->maxElement;  // this instruction will be hit if there are only 1 or 2 different elements
}//Time complexity: best case: Theta(1), worst case: Theta(n), average case Theta(n), Total complexity: O(n)

int Bag::getNewPreviousMax() {
    int index;
    for (index = this->frequencyLength - 2; index >= 0; index--) {
        if (this->frequency[index] != 0) {  // we found a position, different from the one on which the actual max is
            int newPrevMax = index + this->minElement;
            return newPrevMax;  // returning the prev min
        }
    }
    return this->minElement;  // this instruction will be hit if there are only 1 or 2 different elements

}//Time complexity: best case: Theta(1), worst case: Theta(n), average case Theta(n), Total complexity: O(n)

void Bag::addOccurrences(int nr, TElem elem) {
    if (nr <= 0) {
        throw exception();
    }
    if (not search(elem)) {
        add(elem);
        nr--;
    }
    frequency[elem - this->minElement] += nr;
}//Time complexity: best case: Theta(1) , worst case: O(n), average case: O(n), Total complexity: O(n)
