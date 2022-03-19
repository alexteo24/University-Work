#include <assert.h>
#include "Matrix.h"
#include <exception>
using namespace std;

void testAll() { 
	Matrix m(4, 4);
	assert(m.nrLines() == 4);
	assert(m.nrColumns() == 4);	
	m.modify(1, 1, 5);
	assert(m.element(1, 1) == 5);
	TElem old = m.modify(1, 1, 6);
	assert(m.element(1, 2) == NULL_TELEM);
	assert(old == 5);

	// Testing resize
	m.resize(1,1);
	// Checking if nr lines and columns modified properly
    assert(m.nrLines() == 1);
    assert(m.nrColumns() == 1);
    // Trying to access and element out of bound
    try {
        m.element(1, 1);
        assert(false);
    }
    catch (exception&) {
        assert(true);
    }
    assert(m.element(0, 0) == 0);
    m.modify(0, 0, 5);
    assert(m.element(0, 0) == 5);
    // Checking larger resize
    m.resize(4, 4);
    assert(m.nrLines() == 4);
    assert(m.nrColumns() == 4);
    // Checking if older element stayed
    assert(m.element(0, 0) == 5);
    // Inserting new one
    old = m.modify(3, 2, 10);
    // Checking if the element is 0, as intended after the resize
    assert(old == 0);
    // Checking if the modify was successful
    assert(m.element(3, 2) == 10);
    // Shrinking the matrix
    m.resize(1,1);
    // Checking out of bounds again, line 3 element 2 doesnt exist in a matrix with 1 line and 1 column
    try {
        m.element(3, 2);
        assert(false);
    }
    catch (exception&) {
        assert(true);
    }
    // The only element that should have stayed is still here
    assert(m.element(0, 0) == 5);
    // Enlarging the matrix again
    m.resize(4, 4);
    // The element we had before shrinking is gone
    assert(m.element(3, 2) == 0);
    // Testing for exception if newlines and newcols <=0
    try {
        m.resize(0, 0);
        assert(false);
    }
    catch (exception&) {
        assert(true);
    }
}