#include <iostream>
#include "ShortTest.h"
#include <ctime>
#include "ExtendedTest.h"

int main() {
    clock_t tStart = clock();
	testAll();
	testAllExtended();
	std::cout << "Finished LP Tests!" << std::endl;
    printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
	system("pause");
}
