//
// Created by Teo on 3/14/2021.
//

#ifndef A23_ALEXTEO24_UNDOREDO_H
#define A23_ALEXTEO24_UNDOREDO_H
#include "../DynamicArray/DynamicArray.h"

typedef struct {
    dynamicArray * repositoryRecordings;
}undoOperations;

typedef struct {
    dynamicArray * repositoryRecordings;
}redoOperations;

undoOperations * createUndo();

redoOperations * createRedo();

void destroyUndoOperations (undoOperations * someUndoOperations);

void destroyRedoOperations (redoOperations * someRedoOperations);

void addUndoOperation (undoOperations * someUndoOperation, TElem * someRepositoryState);

void addRedoOperation (redoOperations * someRedoOperation, TElem * someRepositoryState);

void deleteUndoOperation (undoOperations * someUndoOperation);

void deleteRedoOperation (redoOperations * someUndoOperation);

#endif //A23_ALEXTEO24_UNDOREDO_H
