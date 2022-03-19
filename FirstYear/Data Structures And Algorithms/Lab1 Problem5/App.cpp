#include "Bag.h"
#include "ShortTest.h"
#include "ExtendedTest.h"
#include <iostream>
#include <ctime>
using namespace std;

int main() {
    clock_t tStart = clock();
	testAll();
	cout << "Short tests over" << endl;

	testAllExtended();
	cout << "All test over" << endl;
    printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    return 0;
}