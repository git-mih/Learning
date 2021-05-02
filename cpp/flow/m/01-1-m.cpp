#include<iostream>
using namespace std;

int main() {
	int N;

	cin >> N;

	/*
	 * lets print the upper triangle first
	 * lets assume N = 4, how many spaces and starts we print
	 * Row 1	Spaces 3	Stars 1
	 * Row 2	Spaces 2	Stars 3
	 * Row 3	Spaces 1	Stars 5
	 * Row 4	Spaces 0	Stars 7
	 *
	 * now we wanna develop formulas for number of spaces and number of starts
	 * for a given 'row'
	 * 	Spaces are: N - rows   	(3, 2, 1, 0)
	 * 	Starts are: 2*row -1	(1, 3, 5, 7)
	 *
	 * now we just iterate for each row
	 * 	print spaces
	 * 	then print starts
	 */
	int row = 1;
	while (row <= N) {
		int stars_count = 1;

		// Print N - rows spaces
		while (stars_count <= N-row) {
			cout << ' ';
			++stars_count;
		}

		// Print 2*rows-1 stars
		stars_count = 1;
		while (stars_count <= 2*row-1) {
			cout << '*';
			++stars_count;
		}
		cout << "\n";
		++row;
	}

	/*
	 * Let's print the lower triangle second
	 * Same logic, we just switch looping from N to 1
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

