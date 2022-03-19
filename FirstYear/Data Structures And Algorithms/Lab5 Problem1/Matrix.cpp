#include "Matrix.h"
#include <exception>
#include <iostream>
using namespace std;


Matrix::Matrix(int nrLines, int nrCols) {
	noLines = nrLines;
	noColumns = nrCols;
	nrElements = 0;
} //Time complexity: Theta(1)


int Matrix::nrLines() const {
	return noLines;
} //Time complexity: Theta(1)


int Matrix::nrColumns() const {
	return noColumns;
} //Time complexity: Theta(1)


TElem Matrix::element(int i, int j) const {
	if(i > noLines - 1 || j > noColumns - 1 || i < 0 || j < 0) {
	    throw exception();
	}
	BSTNode* actualNode = root;
	while (actualNode != nullptr) {
	    if(actualNode->row == i && actualNode->column == j) {
            return actualNode->value;
	    }
	    if(actualNode->row > i || (actualNode->row == i && actualNode->column >= j)) {
	        // should go on the left, since it is "smaller or equal"
	        actualNode = actualNode->leftChild;
	    } else {
	        // should go on the right, since it is "greater"
	        actualNode = actualNode->rightChild;
	    }
	}
	return NULL_TELEM;
} //Time complexity: Best case: Theta(1),
// worst case Theta(h) - h is the height, average case Theta(h), Total complexity: O(h)

TElem Matrix::modify(int i, int j, TElem e) {
    if(i > noLines - 1 || j > noColumns - 1 || i < 0 || j < 0) {
        throw exception();
    }
	if (root == nullptr && e == NULL_TELEM) {
        return NULL_TELEM;
	}
	TElem oldValue = NULL_TELEM;
	if (root == nullptr) {
	    BSTNode* newNode = new BSTNode{};
	    newNode->row = i;
	    newNode->column = j;
	    newNode->value = e;
	    root = newNode;
        nrElements++;
	} else {
	    BSTNode* actualNode = root;
	    BSTNode* previousNode = nullptr;
        while (actualNode != nullptr) {
            if(actualNode->row == i && actualNode->column == j) {
                // actually found our element
                if (e != NULL_TELEM) {
                    // we don't want to remove the element
                    oldValue = actualNode->value;
                    actualNode->value = e;
                    return oldValue;
                } else {
                    // we want to remove the element
                    nrElements--;
                    return removeNode(actualNode);
                }
            } else if (actualNode->row > i || (actualNode->row == i && actualNode->column >= j)) {
                // should go on the left, since it is "smaller or equal"
                previousNode = actualNode;
                actualNode = actualNode->leftChild;
            } else {
                // should go on the right, since it is "greater"
                previousNode = actualNode;
                actualNode = actualNode->rightChild;
            }
        }
        if (e != NULL_TELEM) {
            // the element does not exist, so we want to add it
            BSTNode *newNode = new BSTNode{};
            // passing usual info
            nrElements++;
            newNode->row = i;
            newNode->column = j;
            newNode->value = e;
            // making connections

            // connecting to its parent, in this case previous node
            newNode->parent = previousNode;

            // making connections from parent (should be right or left child)

            if (previousNode->row > i || (previousNode->row == i && previousNode->column >= j)) {
                // the new node will be the left child of the previous
                previousNode->leftChild = newNode;
            } else {
                // the new node will be the right child of the previous
                previousNode->rightChild = newNode;
            }
            return NULL_TELEM;
        }
	}
    return oldValue;
}// Time complexity: Best case Theta(1), worst case Theta(h), average complexity Theta(h), Total complexity O(h)

Matrix::BSTNode *Matrix::findMaximumInLeftSide(Matrix::BSTNode *startNode) {
    BSTNode* actualNode = startNode->leftChild;
    bool changed = false;
    while (actualNode->rightChild != nullptr) {
        actualNode = actualNode->rightChild;
        changed = true;
    }
    if (changed) {
        actualNode->parent->rightChild = nullptr;
    }
    return actualNode;
}// Time complexity: Best case Theta(1), worst case Theta(h), average case Theta(h), Total complexity O(h)

TElem Matrix::removeIfTwoChildren(Matrix::BSTNode *removedNode) {
    TElem oldValue = NULL_TELEM;
    BSTNode* replacementNode = findMaximumInLeftSide(removedNode);
    if(replacementNode == removedNode->leftChild) {
        // the replacement is the immediate left child, so no links on the left should be made
        oldValue = removedNode->value;
        replacementNode->rightChild = removedNode->rightChild;
        replacementNode->rightChild->parent = replacementNode;
        replacementNode->parent = removedNode->parent;
        // deciding what child the replacement node will replace
        if(replacementNode->parent->leftChild == removedNode) {
            // the replacement node will replace the left child of the removed node's parent
            replacementNode->parent->leftChild = replacementNode;
        } else {
            // the replacement node will replace the right child of the removed node's parent
            replacementNode->parent->rightChild = replacementNode;
        }
        BSTNode* nodeForDeletion = removedNode;
        removedNode = replacementNode;
        delete [] nodeForDeletion;
    } else {
        // the replacement is not the immediate left child, so we must make the left links
        oldValue = removedNode->value;
        replacementNode->rightChild = removedNode->rightChild;
        replacementNode->rightChild->parent = replacementNode;
        replacementNode->parent = removedNode->parent;
        // deciding what child the replacement node will replace
        if(replacementNode->parent->leftChild == removedNode) {
            // the replacement node will replace the left child of the removed node's parent
            replacementNode->parent->leftChild = replacementNode;
        } else {
            // the replacement node will replace the right child of the removed node's parent
            replacementNode->parent->rightChild = replacementNode;
        }
        replacementNode->leftChild = removedNode->leftChild;
        replacementNode->leftChild->parent = replacementNode;
        BSTNode* nodeForDeletion = removedNode;
        removedNode = replacementNode;
        delete [] nodeForDeletion;
    }
    return oldValue;
}// Time complexity: Best case Theta(1), worst case Theta(h), average case Theta(h), Total complexity O(h)
TElem Matrix::removeIfOneChildren(Matrix::BSTNode *removedNode) {
    TElem oldValue = removedNode->value;
    if(removedNode->parent->leftChild == removedNode) {
        // the node we want to remove is the left child of his parent
        if(removedNode->leftChild != nullptr) {
            // if he has a left child, we must make the link to its "grandfather"
            removedNode->parent->leftChild = removedNode->leftChild;
            removedNode->leftChild->parent = removedNode->parent;
        } else {
            // if he has a right child, we must make the link to its "grandfather"
            removedNode->parent->leftChild = removedNode->rightChild;
            removedNode->rightChild->parent = removedNode->parent;
        }
        delete [] removedNode;
    } else {
        // the node we want to remove is hte right child of his parent
        if(removedNode->leftChild != nullptr) {
            // if he has a left child, we must make the link to its "grandfather"
            removedNode->parent->rightChild = removedNode->leftChild;
            removedNode->leftChild->parent = removedNode->parent;
        } else {
            // if he has a right child, we must make the link to its "grandfather"
            removedNode->parent->rightChild = removedNode->rightChild;
            removedNode->rightChild->parent = removedNode->parent;
        }
        delete [] removedNode;
    }
    return oldValue;
}// Time complexity: Theta(1)

TElem Matrix::removeIfLeaf(Matrix::BSTNode *removedNode) {
    TElem oldValue = removedNode->value;
    if (removedNode->parent->leftChild == removedNode) {
        // the node we want to remove is the left child of his parent
        removedNode->parent->leftChild = nullptr;
        delete [] removedNode;
    } else if (removedNode->parent->rightChild == removedNode) {
        // the node we want to remove is the right child of his parent
        removedNode->parent->rightChild = nullptr;
        delete [] removedNode;
    }
    return oldValue;
}// Time complexity: Theta(1)

TElem Matrix::removeRootIfLeaf(Matrix::BSTNode *theRoot) {
    TElem oldValue = theRoot->value;
    BSTNode* rootForDeletion = theRoot;
    root = nullptr;
    delete [] rootForDeletion;
    return oldValue;
}// Time complexity: Theta(1)

TElem Matrix::removeRootIfOneChildren(Matrix::BSTNode *theRoot) {
    TElem oldValue;
    if(theRoot->rightChild != nullptr) {
        // the root has a right child
        BSTNode* newRoot = theRoot->rightChild;
        oldValue = theRoot->value;
        BSTNode* rootForDeletion = theRoot;
        newRoot->parent = nullptr;
        root = newRoot;
        delete [] rootForDeletion;
    } else {
        // the root has a left child
        BSTNode* newRoot = theRoot->leftChild;
        oldValue = theRoot->value;
        BSTNode* rootForDeletion = theRoot;
        newRoot->parent = nullptr;
        root = newRoot;
        delete [] rootForDeletion;
    }
    return oldValue;
}// Time complexity: Theta(1)

TElem Matrix::removeRootIfTwoChildren(Matrix::BSTNode *theRoot) {
    BSTNode* replacingNode = findMaximumInLeftSide(theRoot);
    TElem oldValue;
    if(replacingNode == theRoot->leftChild) {
        // max is the immediate left child, so no links on the left should be made
        oldValue = theRoot->value;
        replacingNode->rightChild = theRoot->rightChild;
        replacingNode->rightChild->parent = replacingNode;
        replacingNode->parent = nullptr;
        BSTNode* rootForDeletion = theRoot;
        root = replacingNode;
        delete [] rootForDeletion;
    } else {
        // max is not the immediate left child, so we gotta link on left as well
        oldValue = theRoot->value;
        replacingNode->rightChild = theRoot->rightChild;
        replacingNode->rightChild->parent = replacingNode;
        replacingNode->parent = nullptr;
        replacingNode->leftChild = theRoot->leftChild;
        replacingNode->leftChild->parent = replacingNode;
        BSTNode* rootForDeletion = theRoot;
        root = replacingNode;
        delete [] rootForDeletion;
    }
    return oldValue;
}// Time complexity: Best case Theta(1), worst case Theta(h), average case Theta(h), Total complexity O(h)

TElem Matrix::removeNode(Matrix::BSTNode *removeNode) {
    TElem oldValue = NULL_TELEM;
    if (removeNode == root) {
        // if we want to remove the root
        if (removeNode->rightChild != nullptr && removeNode->leftChild != nullptr) {
            // if root has 2 children
            oldValue = removeRootIfTwoChildren(removeNode);
        } else if (removeNode->rightChild == nullptr && removeNode->leftChild == nullptr) {
            // if root is a leaf
            oldValue = removeRootIfLeaf(removeNode);
        } else {
            // root has only 1 child
            oldValue = removeRootIfOneChildren(removeNode);
        }
    } else {
        // if we want to remove anything other than the root
        if (removeNode->rightChild != nullptr && removeNode->leftChild != nullptr) {
            // if the node we want to remove has 2 children
            oldValue = removeIfTwoChildren(removeNode);
        } else if (removeNode->rightChild == nullptr && removeNode->leftChild == nullptr) {
            // if the node we want to remove is a leaf
            oldValue = removeIfLeaf(removeNode);
        } else {
            // root has only 1 child
            oldValue = removeIfOneChildren(removeNode);
        }
    }
    return oldValue;
}// Time complexity: Best case Theta(1), worst case Theta(h), average case Theta(h), Total complexity O(h)

int Matrix::numberOfNonZeroElems(int line) const {
    BSTNode* startNode = root;
    int dirFlag;
    if (startNode->row >= line) {
        dirFlag = 0;
        while (startNode != nullptr) {
            if (startNode->row > line) {
                startNode = startNode->leftChild;
            } else {break;}
        }
    } else {
        dirFlag = 1;
        while (startNode != nullptr) {
            if (startNode->row < line) {
                startNode = startNode->rightChild;
            } else { break; }
        }
    }
    return getNonZero(startNode, line, dirFlag);
}//Time complexity: Best case Theta(1), worst case Theta(nrElements), Total complexity O(nrElements)

int Matrix::getNonZero(Matrix::BSTNode *someNode, int line, int dirFlag) const {
    if(someNode == nullptr) {
        return 0;
    }
    if (dirFlag == 0) {
        // we went left to find our elements
        if(someNode->row < line) {
            // can find only on the right
            return 0 + getNonZero(someNode->rightChild, line, dirFlag);
        } else if (someNode->row == line) {
            // can find on both left and right
            return 1 + getNonZero(someNode->leftChild, line, dirFlag) + getNonZero(someNode->rightChild, line, dirFlag);
        }
    } else {
        // we went right to find our elements
        if(someNode->row > line) {
            // can find only on the left
            return 0 + getNonZero(someNode->leftChild, line, dirFlag);
        } else if (someNode->row == line) {
            // can find on both left and right
            return 1 + getNonZero(someNode->leftChild, line, dirFlag) + getNonZero(someNode->rightChild, line, dirFlag);
        }
    }
    return 0;
}//Time complexity: best case Theta(1) - no recalls, worst case Theta(nrElements), Total complexity O(nrElements)

