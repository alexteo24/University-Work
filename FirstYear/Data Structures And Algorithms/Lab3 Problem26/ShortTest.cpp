#include "ShortTest.h"

#include <assert.h>
#include <exception>
#include <iostream>


#include "IteratedList.h"
#include "ListIterator.h"



using namespace std;

void testAll() {
	IteratedList list = IteratedList();
	assert(list.size() == 0);
	assert(list.isEmpty());
	list.addToEnd(1);
	assert(list.size() == 1);
	assert(!list.isEmpty());
	ListIterator it = list.search(1);
	assert(it.valid());
	assert(it.getCurrent() == 1);
	it.next();
	assert(!it.valid());
	it.first();
	assert(it.valid());
	assert(it.getCurrent() == 1);
	assert(list.remove(it) == 1);
	assert(list.size() == 0);
	assert(list.isEmpty());

	list.addToEnd(1);
	list.addToEnd(3);
	list.addToEnd(7);
	ListIterator it7 = list.first();
	it7.next();
	it7.next();
    assert(it7.remove() == 7);
    assert(it7.valid() == false);
    try {
        it7.next();
        assert(false);
    }
    catch (exception&) {
        assert(true);
    }
    it7.first();
    assert(it7.getCurrent() == 1);
    it7.next();
    assert(it7.getCurrent() == 3);
    list.addToEnd(7);
    ListIterator it6 = list.first();
    assert(it6.remove() == 1);
    assert(it6.getCurrent() == 3);
    try {
        it6.next();
        assert(true);
    }
    catch (exception&) {
        assert(false);
    }
    list.addToBeginning(1);
    it.next();
    assert(it.getCurrent() == 3);
	ListIterator it3 = list.first();
	list.addToPosition(it3, 77);
	list.addToPosition(it3, 44);
	assert(list.size() == 5);
	ListIterator it2 = list.first();
	assert(it2.getCurrent() == 1);
	it2.next();
	assert(it2.getCurrent() == 77);
	it2.next();
	assert(it2.getCurrent() == 44);
	it2.next();
	assert(it2.getCurrent() == 3);
	it2.next();
	assert(it2.getCurrent() == 7);
	it2.next();
	assert(it2.valid() == false);

	IteratedList list2 = IteratedList();
	list2.addToBeginning(4);
	list2.addToEnd(5);
	list2.addToBeginning(3);
	list2.addToEnd(6);
	list2.addToBeginning(2);
	list2.addToEnd(7);
	int i = 2;
	ListIterator it4 = list2.first();
	while (it4.valid()) {
		assert(it4.getCurrent() == i);
		i++;
		it4.next();
	}
}


