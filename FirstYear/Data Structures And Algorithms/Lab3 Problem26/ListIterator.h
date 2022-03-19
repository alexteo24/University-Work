#pragma once
#include "IteratedList.h"

//DO NOT CHANGE THIS PART
class IteratedList;
typedef int TElem;

class ListIterator{
	friend class IteratedList;
private:
	//TODO - Representation 
    int currentNode;
	//DO NOT CHANGE THIS PART
	IteratedList& list;
	ListIterator(IteratedList& lista);
public:
	void first();
	void next();
	bool valid() const;
    TElem getCurrent() const;
    //Change the iterator to be able to remove the current element. Add the following operation in the SortedListIterator class:
    //
    //removes and returns the current element from the iterator
    //after the operation the current element from the Iterator is the next element from the SortedList, or, if the removed
    //element was the last one, the iterator is invalid
    //throws exception if the iterator is invalid
    TElem remove();
    //
    //Obs: In order for this operation to work, you need to perform some other changes in code:
    //-       Iterator operation from the SortedList no longer is const
    //-       The reference to the  SortedList in the iterator is no longer const (but it is still a reference!)
    //-       The parameter passed to the constructor of the iterator class is no longer const

};


