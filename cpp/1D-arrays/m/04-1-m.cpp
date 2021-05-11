#include <iostream>
using namespace std;

int main() {
    // digit frequency program.
    // for all digits from 0 to 9, we want to know how many times it appeared
    // test case: 2  78 307     
    // better version

    int n, value, occurrence[10] = {0};
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> value;
		if (value == 0)
			occurrence[0]++;

		while (value) {
			int digit = value % 10;
			occurrence[digit]++;
			value /= 10;
		}
	}
	for (int i = 0; i <= 9; i++) {
		cout << i << " " << occurrence[i] << endl;
	}

}


