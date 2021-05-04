#include <iostream>
using namespace std;

int main() {
    // diamond pattern
    // better version
	/*
	  lets print the upper triangle first
	  lets assume N = 4, how many spaces and starts we print
	  Row 1	Spaces 3	Stars 1
	  Row 2	Spaces 2	Stars 3
	  Row 3	Spaces 1	Stars 5
	  Row 4	Spaces 0	Stars 7
	  
	  now we wanna develop formulas for number of spaces and number of starts
	  for a given 'row'
	  	Spaces are: N - rows   	(3, 2, 1, 0)
	  	Starts are: 2*row -1	(1, 3, 5, 7)
	  
	  now we just iterate for each row
	  	print spaces
	  	then print stars
	 */
	int N;
	cin >> N; //test case:  5

	int row = 1;
	while (row <= N) { // row start being 1, then 2, then 3 and so on
		int stars_count = 1;   // gonna use stars_count to print the spaces also

		// Print N - rows spaces
		while (stars_count <= N-row) { // 5-1 // 5-2 // 5-3 // 5-2 // 5-1 
			cout << ' ';               //  4      3      2      1      0     spaces will be printed
			++stars_count;
		}

		// Print 2*rows-1 stars
		stars_count = 1;         //reseting stars_count to print the stars now
		while (stars_count <= 2*row-1) { // 2*1-1 // 2*2-1 // 2*3-1 // 2*4-1 // 2*5-1
			cout << '*';                 //   1        3        5        7        9      stars will be printed
			++stars_count;
		}
		cout << "\n"; // next line
		++row;       // row = 2, 3, 4, 5 
	}

	/*
	  lets print the lower triangle second
	  same logic, we just switch looping from N to 1
	 */
	row = N;
	while (row >= 1) {
		int stars_count = 1;

		while (stars_count <= N-row) {
			cout << ' ';
			++stars_count;
		}

		stars_count = 1;

		while (stars_count <= 2*row-1) {
			cout << '*';
			++stars_count;
		}
		cout << "\n";
		--row;
	}
	return 0;
}

