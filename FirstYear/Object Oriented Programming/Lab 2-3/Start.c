//
// Created by Teo on 3/11/2021.
//
#include "Console/Console.h"
#include "./Domain/TestsDomain.h"
#include "./DynamicArray/TestsDynamicArray.h"
#include "./Repository/TestsRepository.h"
#include "./Service/TestsService.h"
#include "./UndoRedo/TestsUndoRedo.h"
int main() {
    testDomain();
    testDynamicArray();
    testRepository();
    testService();
    testUndoRedo();
    estateRepository * Repository = createEstateRepository(10);
    initRepository(Repository);
    estateService * Service = createEstateService(Repository);
    Console * theConsole = createConsole(Service);
    runProgram(theConsole);
    return 0;
}
