#include <iostream>
#include <cassert>
using namespace std;

int main() {
    // program which read a integer n (<1000), then read n integers (0 <= n <= 500)
    // the n numbers are ordered in ascending order.
    // we require to print the UNIQUE list of numbers, preserving the given order.
    // eg:    input:  12        1 1 2 2 2 5 6 6 7 8 9 9 (im using assert() to guarantee the ascending order)
    //       output: 1 2 5 6 6 7 8 9 9  

	int arr[1000];

	int n; 
	cin >> n;

	for (int i = 0; i < n; i++)
		cin >> arr[i];

	cout << arr[0] << " ";

	for (int i = 1; i < n; i++) {
		assert(arr[i] >= arr[i-1]); 

		if (arr[i] != arr[i-1])
			cout << arr[i]<<" ";
	}

	return 0;
}

