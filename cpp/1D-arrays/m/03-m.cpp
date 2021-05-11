#include <iostream>
using namespace std;

int main() {
    // program which read a integer n then read n numbers. And then find the value that repeated the most number of times
    // each integer is -500 <= value <= 270
    // eg:  input:  7     -1 2 -1 3 -1 5 5
    //      output: -1 repeated 3 times

	int n;
	cin >> n;  // test case: 7

	const int MAX = 270 + 500 + 1; // MAX = 771
	int frequency[MAX] = { 0 };	// initialize with zeros. we cant do for other values (eg. 1) this way

	for (int i = 0; i < n; i++) { // 6<7
		int value;
		cin >> value;  // 5   505

		value += 500;	// shift all values to be positive
		frequency[value]++; // a[499] = 3 // a[502] = 1 // a[503] = 1 // a[505] = 2
	}

	int mx_pos = 0; // max_pos var come to picture
	for (int i = 0; i < MAX; i++) { // 0 < 771
		if (frequency[mx_pos] < frequency[i]) // a[0] < a[499]     (0 < 3)  (3 < 1) (3 < 1) (3 < 2) 
			mx_pos = i; //    mx_pos = 499
	}

	cout << mx_pos - 500 << " has repeated " << frequency[mx_pos] << " times ";
    //     499 - 500 = -1                            a[499] = 3

    return 0;
}

