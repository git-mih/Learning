#include <iostream>
using namespace std;

int main() {
    // program which read a integer n and print the first n numbers that are:
    // multiple of 3 but not multiple of 4int n;
    // another way
    int n;
	cin >> n; // test case: 11     output: 3 6 9 15 18 21 27 30 33 39 42

	int i = 0;
	int current_number = 0;

	while (i < n) { // (0<11  0<11  0<11) (1<11)
		if (current_number % 3 == 0 && current_number % 4 != 0) { // (0%3==0 && 0%4!=0) (1%3==0 && 1%4!=0) (2%3==0 ...) (3%3==0 && 3%4!==0)
			cout << current_number << " "; //                             T      F          F        T        F     T        T      T
			i++; // i=1    
		}
		current_number++;   // current_number = 1  2 (3) 4  5 (6) ...
	}

	return 0;
}