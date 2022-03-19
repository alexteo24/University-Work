#include <assert.h>
#include "Matrix.h"
#include <iostream>

using namespace std;

void testAll() { 
	Matrix m(4, 4);
	assert(m.nrLines() == 4);
	assert(m.nrColumns() == 4);	
	m.modify(1, 1, 5);
	assert(m.element(1, 1) == 5);
	TElem old = m.modify(1, 1, 6);
    assert(old == 5);
    // there should be only 1 element on line 1
    assert(m.numberOfNonZeroElems(1) == 1);
    // adding a new element on line 1
    old = m.modify(1, 3 ,5);
    assert(old == NULL_TELEM);
    assert(m.element(1, 3) == 5);
    assert(m.numberOfNonZeroElems(1) == 2);
    assert(m.element(1, 2) == NULL_TELEM);

    // adding elements on other lines
    old = m.modify(2, 3 ,5);
    assert(old == NULL_TELEM);
    assert(m.element(2, 3) == 5);

    old = m.modify(3, 3 ,5);
    assert(old == NULL_TELEM);
    assert(m.element(3, 3) == 5);

    old = m.modify(0, 3 ,5);
    assert(old == NULL_TELEM);
    assert(m.element(0, 3) == 5);
    // should be the same
    assert(m.numberOfNonZeroElems(1) == 2);

    old = m.modify(0, 2 ,5);
    assert(old == NULL_TELEM);
    assert(m.element(0, 2) == 5);

    old = m.modify(1, 0 ,5);
    assert(old == NULL_TELEM);
    assert(m.element(1, 0) == 5);

    old = m.modify(1, 2 ,5);
    assert(old == NULL_TELEM);
    assert(m.element(1, 2) == 5);

    assert(m.numberOfNonZeroElems(1) == 4);
    assert(m.numberOfNonZeroElems(0) == 2);
    assert(m.numberOfNonZeroElems(2) == 1);
    old = m.modify(2, 2 ,5);
    assert(old == NULL_TELEM);
    assert(m.element(2, 2) == 5);
    assert(m.numberOfNonZeroElems(2) == 2);
    assert(m.numberOfNonZeroElems(3) == 1);
    m.modify(3, 3, NULL_TELEM);
    assert(m.numberOfNonZeroElems(3) == 0);
    cout<<"Tests for extra operation done...\n";
}