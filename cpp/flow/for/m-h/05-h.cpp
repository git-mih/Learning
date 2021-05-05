#include<iostream>
using namespace std;

int main() {
    // program which get an integer n (1 < n < 500) then print all prime numbers <= n.
    //    output should be comma separated
    //        dont print comma at the last number   
    // n = 18    output: 2,3,5,7,11,13,17 

	bool first_print = true; //fp = 1

	int target; 
	cin >> target; //  18

	for (int n = 2; n <= target; n++) { // n=2 <=18 // n=3 <=18 // n=4 <= 18 // ...
		bool is_prime = true; // ok = 1

		for (int i = 2; i < n; ++i) { // i=2 <2 // i=2 < 3          // i=2 <4
			if (n % i == 0) {                   //  3 % 2 == 0? no. // 4%2 == 0? yes.
				is_prime = false;
				break;
			}
		}

		if (is_prime) // 1    // when n=4, is_prime will become false and we wont print it.
		{
			if(!first_print) // fp = 0
				cout<<",";  // 2,

			cout << n; // 2 3

			first_print = false; // fp = 0
		}
	}

	return 0;
}