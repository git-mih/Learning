#include <iostream>
using namespace std;

int main() {
    // program which find the minimum 3 values
    // it will read a integer n (n >= 3), then read n integers. Finding the 3 lowest numbers
    // eg:  input:   5    4 1 3 10 8    output: 1 3 4
    //               3    7 9 -2               -2 7 9

	int n, tmp, min[3];

	cin >> n;
	for (int i = 0; i < n; i++) {
		int value;
		cin >> value;

		if (i < 3)
			min[i] = value;
		else {
			// Find maximum position
			int mx_pos = 0;
			for (int j = 1; j < 3; ++j) {
				if (min[mx_pos] < min[j])
					mx_pos = j;
			}

			if (value < min[mx_pos])
				min[mx_pos] = value;
		}
	}

	// let's order the first 3 values. We can do in several ways
	// Find maximum position
	int mx_pos = 0;
	for (int j = 1; j < 3; ++j) {
		if (min[mx_pos] < min[j])
			mx_pos = j;
	}
	// swap max with last
	tmp = min[2];
	min[2] = min[mx_pos];
	min[mx_pos] = tmp;

	// Swap first 2 elements if needed
	if (min[0] > min[1]) {
		tmp = min[0];
		min[0] = min[1];
		min[1] = tmp;
	}

	for (int i = 0; i < 3; i++)
		cout << min[i] << " ";	// not ordered


	return 0;
}