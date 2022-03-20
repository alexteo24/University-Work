cmake_minimum_required(VERSION 3.20)
project(Lab_8_9)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_PREFIX_PATH "C:\\Qt\\5.15.2\\mingw81_64\\")
set(QT_VERSION 5)
set(REQUIRED_LIBS Core Gui Widgets)
set(REQUIRED_LIBS_QUALIFIED Qt5::Core Qt5::Gui Qt5::Widgets Qt5::Charts)

add_executable(${PROJECT_NAME} start.cpp
        ConsoleAdministrator/ConsoleAdministrator.cpp
        ConsoleAdministrator/ConsoleAdministrator.h
        ConsoleUser/ConsoleUser.cpp
        ConsoleUser/ConsoleUser.h
        Domain/Coat.cpp
        Domain/Coat.h
        RepositoryCoats/ExceptionsRepoCoats.cpp
        RepositoryCoats/ExceptionsRepoCoats.h
        RepositoryCoats/RepositoryCoats.cpp
        RepositoryCoats/RepositoryCoats.h
        RepositoryCoats/RepositoryCoatsFile.cpp
        RepositoryCoats/RepositoryCoatsFile.h
        RepositoryShopping/RepostioryShopping.cpp
        RepositoryShopping/RepostioryShopping.h
        ServiceAdmin/ServiceAdministrator.cpp
        ServiceAdmin/ServiceAdministrator.h
        ServiceUser/ServiceUser.cpp
        ServiceUser/ServiceUser.h
        ServiceUser/ShoppingExceptions.cpp
        ServiceUser/ShoppingExceptions.h
        Validators/ValidatorCoat.cpp
        Validators/ValidatorCoat.h
        GUI.cpp
        GUI.h)

if (NOT CMAKE_PREFIX_PATH)
    message(WARNING "CMAKE_PREFIX_PATH is not defined, you may need to set it "
            "(-DCMAKE_PREFIX_PATH=\"path/to/Qt/lib/cmake\" or -DCMAKE_PREFIX_PATH=/usr/include/{host}/qt{version}/ on Ubuntu)")
endif ()

find_package(Qt5 COMPONENTS Widgets Charts REQUIRED)
find_package(Qt${QT_VERSION} COMPONENTS ${REQUIRED_LIBS} REQUIRED)
target_link_libraries(${PROJECT_NAME} ${REQUIRED_LIBS_QUALIFIED})