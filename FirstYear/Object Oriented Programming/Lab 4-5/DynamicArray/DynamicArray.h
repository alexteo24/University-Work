//
// Created by Teo on 3/16/2021.
//

#ifndef A45_ALEXTEO24_DYNAMICARRAY_H
#define A45_ALEXTEO24_DYNAMICARRAY_H
#pragma once
#include <stdexcept>

template<typename TElem>

class dynamicArray {
private:
    TElem * elements;
    int capacity;
    int length;

public:
    dynamicArray (int capacity);

    dynamicArray (const dynamicArray &arrayForCopy);

    ~dynamicArray();

    void addElement(const TElem &element);

    void deleteElement(const TElem &element);

    void updateElement(const TElem &newElement, const TElem &oldElement);

    int getLength();

    int findElement(const TElem &element);

    TElem& operator[](int position);

    dynamicArray& operator=(const dynamicArray& newArray);

    void setLength(int length);

    void resizeArray();
};

template <typename TElem>
dynamicArray<TElem>::dynamicArray (int capacity)
/// Creating dynamic array
/// \tparam TElem - the type of elements
/// \param capacity - the capacity of the array
{
    this->capacity = capacity;
    this->length = 0;
    this->elements = new TElem [this->capacity];
}

template <typename TElem>
dynamicArray<TElem>::dynamicArray(const dynamicArray<TElem> &arrayForCopy)
/// Copy constructor
/// \tparam TElem - the type of elements
/// \param arrayForCopy - the array we want to copy
{
    capacity = arrayForCopy.capacity;
    length = arrayForCopy.length;
    elements = new TElem[capacity];
    int index;
    for (index = 0; index < length; index++) {
        elements[index] = arrayForCopy.elements[index];
    }
}

template <typename TElem>
dynamicArray<TElem>::~dynamicArray() {
    delete [] elements;
}

template <typename TElem>
void dynamicArray<TElem>::resizeArray()
/// Resizing the array
/// \tparam TElem - type of elements
{
    TElem * newArray = new TElem [this->capacity * 2];
    int index;
    for (index = 0; index < this->length; index++) {
        newArray[index] = this->elements[index];
    }
    delete [] this->elements;
    this->elements = newArray;
    capacity *= 2;
}

template <typename TElem>
/// Operator overload
TElem &dynamicArray<TElem>::operator[](int position) {
    if (position < 0 or position >= length) {
        throw std::out_of_range("Invalid position!");
    }
    return elements[position];
}

template <typename TElem>
void dynamicArray<TElem>::addElement(const TElem &element)
/// Adding a new element to the array
/// \tparam TElem - the type of elements
/// \param element - the element we want to add
{
    if (capacity == length) {
        resizeArray();
    }
    elements[length] = element;
    length++;
}

template <typename TElem>
int dynamicArray<TElem>::findElement(const TElem &element)
/// Searching for an element
/// \tparam TElem - the type of elements
/// \param element - the element we want to search
/// \return - the position of the element in the array or -1 if it does not exist
{
    int index;
    for (index = 0; index < capacity; index++){
        if (elements[index] == element) {
            return index;
        }
    }
    return -1;
}

template <typename TElem>
void dynamicArray<TElem>::deleteElement(const TElem &element)
/// Deleting an element, if it exists
/// \tparam TElem - the type of elements
/// \param element - the element we want to delete
{
    int index = findElement(element);
    if (index != -1) {
        elements[index] = elements[length - 1];
        length--;
    }
}

template <typename TElem>
void dynamicArray<TElem>::updateElement(const TElem &newElement, const TElem &oldElement)
/// Updating an element, if the one we want to update exists
/// \tparam TElem - the type of elements
/// \param newElement - the element with the new data
/// \param oldElement - the element with the old data
{
    int index = findElement(oldElement);
    if (index != -1) {
        elements[index] = newElement;
    }
}

template <typename TElem>
/// Operator overload
dynamicArray<TElem>& dynamicArray<TElem>::operator=(const dynamicArray<TElem> &newArray) {
    if (this != &newArray) {
        if (capacity < newArray.length) {
            delete [] elements;
            elements = new TElem[newArray.capacity];
        }
        int index;
        length = newArray.length;
        for ( index = 0; index < length; index++) {
            elements[index] = newArray.elements[index];
        }
    }
    return *this;
}

template <typename TElem>
int dynamicArray<TElem>::getLength() {
    return length;
}

template <typename TElem>
void dynamicArray<TElem>::setLength(int someLength) {
    length = someLength;
}


#endif //A45_ALEXTEO24_DYNAMICARRAY_H
