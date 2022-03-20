//
// Created by Teo on 3/14/2021.
//

#include "UndoRedo.h"
#include <stdlib.h>
#include "../Repository/Repository.h"
undoOperations * createUndo() {
    undoOperations * newUndoOperations = (undoOperations *)malloc(sizeof(undoOperations));
    newUndoOperations->repositoryRecordings = createDynamicArray(10);
    return newUndoOperations;
}

redoOperations * createRedo() {
    redoOperations * newRedoOperations = (redoOperations *)malloc(sizeof (redoOperations));
    newRedoOperations->repositoryRecordings = createDynamicArray(10);
    return newRedoOperations;
}

void destroyUndoOperations (undoOperations * someUndoOperations) {
    int index;
    for (index = 0; index < someUndoOperations->repositoryRecordings->length; index++) {
        destroyEstateRepository((estateRepository *) someUndoOperations->repositoryRecordings->elements[index]);
    }
    destroyDynamicArray(&someUndoOperations->repositoryRecordings);
    free(someUndoOperations);
}

void destroyRedoOperations (redoOperations * someRedoOperations) {
    int index;
    for (index = 0; index < someRedoOperations->repositoryRecordings->length; index++) {
        destroyEstateRepository(someRedoOperations->repositoryRecordings->elements[index]);
    }
    destroyDynamicArray(&someRedoOperations->repositoryRecordings);
    free(someRedoOperations);
}

void addUndoOperation (undoOperations * someUndoOperation, TElem * someRepositoryState) {
    addElement(someUndoOperation->repositoryRecordings, someRepositoryState);
}

void addRedoOperation (redoOperations * someRedoOperation, TElem * someRepositoryState) {
    addElement(someRedoOperation->repositoryRecordings, someRepositoryState);
}

void deleteUndoOperation (undoOperations * someUndoOperation) {
    int deletePosition = someUndoOperation->repositoryRecordings->length - 1;
    deleteElement(someUndoOperation->repositoryRecordings, deletePosition);
}

void deleteRedoOperation (redoOperations * someRedoOperation) {
    int deletePosition = someRedoOperation->repositoryRecordings->length - 1;
    deleteElement(someRedoOperation->repositoryRecordings, deletePosition);
}
