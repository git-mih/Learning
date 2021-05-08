#include <iostream>
using namespace std;

int main () {
    // another way of doing it, without using Array
    int n;
	cin >> n;

	int last_value = -1;
	for (int i = 0; i < n; i++) {
		int value;
		cin >> value;

		if (value != last_value)
			cout << value << " ";

		last_value = value;
	}

    return 0;
}