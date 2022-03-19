#include "MultiMapIterator.h"
#include "MultiMap.h"


MultiMapIterator::MultiMapIterator(const MultiMap& c): col(c) {
    start = col.head;
}
//Time complexity: Theta(1)

TElem MultiMapIterator::getCurrent() const{
    if (!(valid())) {
        throw exception();
    }
    else
	    return start->info;
}
//Time complexity: Theta(1)

bool MultiMapIterator::valid() const {
	if (start == nullptr) {
        return false;
	}
	return true;
}
//Time complexity: Theta(1)

void MultiMapIterator::next() {
	if (! valid()) {
        throw exception();
	}
	start = start->next;
}
//Time complexity: Theta(1)

void MultiMapIterator::first() {
    start = col.head;
}
//Time complexity: Theta(1)

