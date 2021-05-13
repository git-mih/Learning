#include<iostream>
using namespace std;

int main() {
    //another way
	int n;
	cin >> n; // 4

	int row = 1;
	while (row <= n) { // (1<=4) (2<=4) (3<=4) (4<=4)
		int stars_count = 1; // good practice to keep this variable local to this while function

		while (stars_count <= row) { // (4<=4)
			cout << '*'; // *   **   ***   ****
			++stars_count;
		}
		cout << "\n";
		row++;
	}

	return 0;
}