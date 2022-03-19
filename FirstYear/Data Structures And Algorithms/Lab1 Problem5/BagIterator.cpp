#include <exception>
#include "BagIterator.h"
#include "Bag.h"
using namespace std;


BagIterator::BagIterator(const Bag& c): bag(c)
{
	this->current = 0;
	currElem = bag.minElement;
	currElemNr = bag.frequency[this->current];
}//Time complexity: Theta(1)

void BagIterator::first() {
	this->current = 0;
    currElem = bag.minElement;
    currElemNr = bag.frequency[this->current];
}//Time complexity: Theta(1)


void BagIterator::next() {
	if(not(this->valid())) {
        throw exception();
    }
	// we already are on an element, so we must decrease its frequency
    this->currElemNr--;
	if (this->currElemNr == 0) {  // if its frequency its now 0, we must look for a new position for which frequency[pos] !=0
	    this->current++;
        while (bag.frequency[this->current] == 0 and (this->valid())) {  // as long as we didn't find a new elem
            this->current++;
            }
        this->currElemNr = bag.frequency[this->current];  // get current element frequency
        currElem = bag.minElement + this->current;  // get the value of the current element
    }
}//Time complexity: BestCaste Theta(1) WorstCase Theta(n) AverageCase Theta(n)


bool BagIterator::valid() const {
    if (this->current < this->bag.frequencyLength) {
        return true;
    }
    return false;
}//Time complexity: Theta(1)



TElem BagIterator::getCurrent() const {
	if (not(this->valid())) {
        throw exception();
    }
	else
        return this->currElem;
}//Time complexity: Theta(1)