//
// Created by Teo on 3/11/2021.
//

#include "DynamicArray.h"
#include <stdlib.h>

dynamicArray * createDynamicArray(int capacity)
/// This function creates a new dynamic array having a given capacity
/// \param capacity - the capacity we want for the new dynamic array
/// \return - the address of the dynamic array
{
    dynamicArray * newDynamicArray = (dynamicArray*)malloc(sizeof (dynamicArray));
    newDynamicArray->elements = (TElem*)malloc(capacity*sizeof (TElem));
    newDynamicArray->capacity = capacity;
    newDynamicArray->length = 0;
    return newDynamicArray;
}

void destroyDynamicArray(dynamicArray ** someDynamicArray)
/// This function is responsible for destroying a dynamic array
/// \param someDynamicArray - the dynamic array we want to destroy
{
    free((*someDynamicArray)->elements);
    free(*someDynamicArray);
}

void addElement(dynamicArray * someDynamicArray, TElem newElement)
/// This function is responsible for adding a new element to a dynamic array
/// \param someDynamicArray - the dynamic array to which we want to add the element
/// \param newElement - the element we want to add
{
    if (arrayCapacity(someDynamicArray) == arrayLength(someDynamicArray)) {
        resizeArray(someDynamicArray);
    }
    someDynamicArray->elements[arrayLength(someDynamicArray)] = newElement;
    someDynamicArray->length++;
}

void deleteElement(dynamicArray * someDynamicArray, int deletePosition)
/// This function is responsible for deleting the element found on a certain position in the dynamic array
/// \param someDynamicArray - the dynamic array from which we want to remove an element from a certain position
/// \param deletePosition - the position on which the element we want to remove is
{
    if (deletePosition == arrayLength(someDynamicArray) - 1) {
        someDynamicArray->length--;
    }
    else {
        someDynamicArray->elements[deletePosition] = someDynamicArray->elements[(arrayLength(someDynamicArray)) - 1];
        someDynamicArray->length--;
    }
}

void updateElement(dynamicArray * someDynamicArray, int updatePosition, TElem updatedElement)
/// This function is responsible for updating the element found on a certain position in the dynamic array
/// \param someDynamicArray - the dynamic array in which the element we want to update should be
/// \param updatePosition - the position in the dynamic array on which the element we want to update is
/// \param updatedElement - the element with updated data
{
    someDynamicArray->elements[updatePosition] = updatedElement;
}

void resizeArray(dynamicArray * someDynamicArray)
/// This function is responsible for resizing a dynamic array by doubling it's capacity
/// \param someDynamicArray - the dynamic array we want to resize
{
    TElem * newList = (TElem*)malloc(someDynamicArray->capacity * 2 * sizeof(TElem));
    int index;
    for (index = 0; index < someDynamicArray->length; index++) {
        newList[index] = someDynamicArray->elements[index];
    }
    free(someDynamicArray->elements);
    someDynamicArray->elements = newList;
    someDynamicArray->capacity *= 2;
}

int arrayCapacity(dynamicArray * someDynamicArray) {
    return someDynamicArray->capacity;
}

int arrayLength(dynamicArray * someDynamicArray) {
    return someDynamicArray->length;
}

TElem getElement(dynamicArray * someDynamicArray, int elementPosition) {
    return someDynamicArray->elements[elementPosition];
}