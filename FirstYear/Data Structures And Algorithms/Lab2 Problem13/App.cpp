#include <iostream>
#include <ctime>
#include "MultiMap.h"
#include "ExtendedTest.h"
#include "ShortTest.h"
#include "MultiMapIterator.h"

using namespace std;


int main() {
    clock_t tStart = clock();
	testAll();
	testAllExtended();
	cout << "End" << endl;
    printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    system("pause");

}
