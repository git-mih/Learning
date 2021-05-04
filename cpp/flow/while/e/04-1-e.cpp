#include<iostream>
using namespace std;

int main() {
    // another way
	int n;
	cin >> n; // 3

	int row = n; // row = 3 
	while (row > 0) { // (3>0) (2>0) (1>0)
		int stars_count = 1;

		while (stars_count <= row) { // (1<=3, 2<=3, 3<=3) (1<=2, 2<=2) (1<=1)
			cout << '*'; //                     ***            **         *
			++stars_count;
		}
		cout << "\n";
		row--;
	}

	return 0;