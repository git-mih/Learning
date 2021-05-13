#include<iostream>
using namespace std;

int main() {
    // program which read a integer n, then print its reverse integer R and R*3
    // input:  123
    // output: 321 963
    // better way
	int n;
	cin >> n; // 123

	int number = 0;

	while (n > 0) {  //                     (123 > 0)  (12 > 0)  (1 > 0)
		int last_digits = n % 10;  // last_digits = 3      2        1
		n /= 10;	//                          n = 12     1        0

		number = number * 10 + last_digits; // (number = 0*10 + 3)   (3*10 + 2)    (32*10 + 1)
	}                                       //  number = 3           number = 32     number = 321
	cout << number << " " << number * 3 << "\n"; // 321 963

	return 0;
}

