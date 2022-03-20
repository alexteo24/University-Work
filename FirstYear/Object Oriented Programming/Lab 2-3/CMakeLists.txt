cmake_minimum_required(VERSION 3.20)
project(Lab_2_3 C)

set(CMAKE_C_STANDARD 99)

add_executable(Lab_2_3 Start.c
        Console/Console.c
        Console/Console.h
        Domain/Domain.c
        Domain/Domain.h
        Domain/TestsDomain.c
        Domain/TestsDomain.h
        DynamicArray/DynamicArray.c
        DynamicArray/DynamicArray.h
        DynamicArray/TestsDynamicArray.c
        DynamicArray/TestsDynamicArray.h
        Repository/Repository.c
        Repository/Repository.h
        Repository/TestsRepository.c
        Repository/TestsRepository.h
        Service/Service.c
        Service/Service.h
        Service/TestsService.c
        Service/TestsService.h
        UndoRedo/UndoRedo.c
        UndoRedo/UndoRedo.h
        UndoRedo/TestsUndoRedo.c
        UndoRedo/TestsUndoRedo.h)
