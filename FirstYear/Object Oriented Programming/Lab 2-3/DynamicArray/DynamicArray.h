//
// Created by Teo on 3/11/2021.
//

#ifndef A23_ALEXTEO24_DYNAMICARRAY_H
#define A23_ALEXTEO24_DYNAMICARRAY_H

typedef void* TElem;

typedef struct {
    TElem * elements;
    int capacity;
    int length;
}dynamicArray;

dynamicArray * createDynamicArray(int capacity);

void destroyDynamicArray(dynamicArray ** someDynamicArray);

void addElement(dynamicArray * someDynamicArray, TElem newElement);

void deleteElement(dynamicArray * someDynamicArray, int deletePosition);

void updateElement(dynamicArray * someDynamicArray, int updatePosition, TElem updatedElement);

void resizeArray(dynamicArray * someDynamicArray);

int arrayCapacity(dynamicArray * someDynamicArray);

int arrayLength(dynamicArray * someDynamicArray);

TElem getElement(dynamicArray * someDynamicArray, int elementPosition);

#endif //A23_ALEXTEO24_DYNAMICARRAY_H
