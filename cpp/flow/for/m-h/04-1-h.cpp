#include<iostream>
using namespace std;

int main() {
    // program which read an integer n (2 < n < 500) and print YES if it is prime, otherwise print NO.
    // another way
	int n;
	cin >> n; // test case: 4 // 5

	if (n <= 1)
		cout << "NO\n";
	else {
		bool is_prime = true; // is_prime = 1

		for (int i = 2; i < n; ++i) { // i=2 < 4         | i=2 < 5      // i=3 < 5      // i=4 < 5
			if (n % i == 0) {         // 4%2 == 0? yes.  | 5%2 == 0? no // 5%3 == 0? no // 5%4 == 0? no
				is_prime = false; 
				break;
			}
		}
		if (is_prime) 
			cout << "YES";
		else
			cout << "NO";
	}

	return 0;
}