#pragma once

//DO NOT CHANGE THIS PART
typedef int TElem;
#define NULL_TELEM 0

class Matrix {

private:
	struct BSTNode {
	    int row = -1;
	    int column = -1;
	    TElem value = NULL_TELEM;
	    BSTNode* parent = nullptr;
	    BSTNode* leftChild = nullptr;
	    BSTNode* rightChild = nullptr;
	};
	BSTNode* root = nullptr;
	int noLines;
	int noColumns;
	int nrElements;
public:
	//constructor
	Matrix(int nrLines, int nrCols);

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

    //returns the number of non-zero elements from a given line
    //throws an exception if line is not valid
    int numberOfNonZeroElems(int line) const;


private:
    static BSTNode* findMaximumInLeftSide(BSTNode* startNode);

    TElem removeIfTwoChildren(BSTNode* removedNode);

    TElem removeIfOneChildren(BSTNode* removedNode);

    TElem removeIfLeaf(BSTNode* removedNode);

    TElem removeRootIfLeaf(BSTNode* theRoot);

    TElem removeRootIfOneChildren(BSTNode* theRoot);

    TElem removeRootIfTwoChildren(BSTNode* theRoot);

    TElem removeNode(BSTNode* removeNode);

    int getNonZero(BSTNode* someNode, int line, int dirFlag) const;
};
