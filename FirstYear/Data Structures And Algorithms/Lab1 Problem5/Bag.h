#pragma once
//DO NOT INCLUDE BAGITERATOR


//DO NOT CHANGE THIS PART
#define NULL_TELEM -111111;
typedef int TElem;
class BagIterator; 
class Bag {

private:
	int nrElements;
    int maxElement;
    int minElement;
    int* frequency;
    int frequencyCap;
    int frequencyLength;
    int previousMin;
    int previousMax;


	//DO NOT CHANGE THIS PART
	friend class BagIterator;
public:
	//constructor
	Bag();

	//adds an element to the bag
	void add(TElem e);

	//removes one occurrence of an element from a bag
	//returns true if an element was removed, false otherwise (if e was not part of the bag)
	bool remove(TElem e);

	//checks if an element appears is the bag
	bool search(TElem e) const;

	//returns the number of occurrences for an element in the bag
	int nrOccurrences(TElem e) const;

	//returns the number of elements from the bag
	int size() const;

    //adds nr occurrences of elem in the Bag (if elem was not in the bag, it will still be added).
    //throws an exception if nr is negative
    void addOccurrences(int nr, TElem elem);


    //returns an iterator for this bag
	BagIterator iterator() const;

	//checks if the bag is empty
	bool isEmpty() const;

	//destructor
	~Bag();

private:
    // shifts a number of positions to the right, the number of position is being determined inside the function
    void shiftElementsRight();
    // shifts a number of positions to the left, the number of position is being determined inside the function
    void shiftElementsLeft();
    // determines and returns the previous min element
    int getNewPreviousMin();
    // determines and returns the previous max element
    int getNewPreviousMax();
};