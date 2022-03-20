//
// Created by Teo on 3/14/2021.
//

#include "TestsUndoRedo.h"
#include <stdio.h>
#include <assert.h>
void testUndoRedo() {
    printf("\nTesting Undo Redo!\n");
    undoOperations * someUndo = createUndo();
    redoOperations *someRedo = createRedo();
    estateRepository * newRepository = createEstateRepository(10);
    initRepository(newRepository);
    estateRepository * newRepository2 = createEstateRepository(10);
    initRepository(newRepository2);
    estateRepository * newRepository3 = createEstateRepository(10);
    initRepository(newRepository3);
    estateRepository * newRepository4 = createEstateRepository(10);
    addUndoOperation(someUndo, (TElem *) newRepository);
    assert(someUndo->repositoryRecordings->length == 1);
    addUndoOperation(someUndo, (TElem *) newRepository2);
    assert(someUndo->repositoryRecordings->length == 2);
    addRedoOperation(someRedo, (TElem *) newRepository3);
    assert(someRedo->repositoryRecordings->length == 1);
    addRedoOperation(someRedo, (TElem *) newRepository4);
    assert(someRedo->repositoryRecordings->length == 2);
    destroyEstateRepository(newRepository2);
    deleteUndoOperation(someUndo);
    assert(someUndo->repositoryRecordings->length == 1);
    destroyEstateRepository(newRepository4);
    deleteRedoOperation(someRedo);
    assert(someRedo->repositoryRecordings->length == 1);
    destroyUndoOperations(someUndo);
    destroyRedoOperations(someRedo);
    printf("\nDone!\n");
}
