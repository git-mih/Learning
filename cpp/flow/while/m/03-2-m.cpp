#include <iostream>
using namespace std;

int main() {
    // program which read a integer n and print the first n numbers that are:
    // multiple of 3 but not multiple of 4int n;
    // More efficient way is to jump 3s
    int n;
	cin >> n; // test case: 11        output: 3 6 9 15 18 21 27 30 33 39 42

	int start = 3;
	while (n) {   // n=11  10 9 8 7...                                    False, cause it is == 0 so we just go next iteration without printing
		if(start % 4 != 0)	// (3 % 4 != 0) (6 % 4 != 0) (9 % 4 != 0) (12 % 4 != 0) ...
			--n, cout<<start<<" "; // n=10, 9 8 7...  and printing: 3 6 9 15 ...
		start += 3;	// start = 3+3 = 6
	}               // start = 6+3 = 9
	                // start = 9+3 = 12
	                // start = 12+3 = 15
	return 0;
}