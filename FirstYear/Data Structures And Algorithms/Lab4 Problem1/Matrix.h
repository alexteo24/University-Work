#pragma once

//DO NOT CHANGE THIS PART
typedef int TElem;
#define NULL_TELEM 0

class Matrix {

private:
	struct Node {
	    int row = -1;
	    int column = -1;
        TElem info = NULL_TELEM;
        Node* next = nullptr;
	};
	Node** hashtable;
	int nrElements;
	int noLines;
	int noColumns;
	int capacity;

	void resizeAndRehash();
public:
	//constructor
	Matrix(int nrLines, int nrCols);

	~Matrix();

	//returns the number of lines
	int nrLines() const;

	//returns the number of columns
	int nrColumns() const;

	//returns the element from line i and column j (indexing starts from 0)
	//throws exception if (i,j) is not a valid position in the Matrix
	TElem element(int i, int j) const;

	//modifies the value from line i and column j
	//returns the previous value from the position
	//throws exception if (i,j) is not a valid position in the Matrix
	TElem modify(int i, int j, TElem e);

    //resizes a Matrix to a given dimension. If the dimensions are less than the current dimensions,
    // elements from positions no longer existing will disappear. If the dimensions are greater than the current
    // dimensions, all new elements will be by default NULL_TELEM.
    //throws exception if the new dimensions are zero or negative
    void resize(int newLines, int newCol);

};
