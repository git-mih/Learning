#include <iostream>
using namespace std;

int main() {
    // program which read a integer T for a number of test cases
    // for each test case, read a integer N followed by reading N integers and then print the minimum value of the n integers
    // better way

    // test case: 2   6 (10 50 30 20 70 4) output: 4 is the minimum value in this case
    //                3 (10 5 30) output: 5 is the minimum

	int T;
	cin >> T; // 2

	while (T) { // 2  1
		int n;
		cin >> n; // 6

		int pos = 0;
		int result;

		while (pos < n) { // 0<6  1<6  2<6  3<6  4<6  5<6
			int value;
			cin >> value; // 10   50   30   20   70   4

			if (pos == 0) // (0 == 0) (1 != 0) (2 != 0) ... 
				result = value; // result = 10 when pos = 0
			else if (result > value) // (10>20) ... (10>4)
				result = value; //        F            T
                                //                 result = 4
			pos++; // pos=1  2 3 4 5 
		}
		cout<<result<<"\n"; // T = 2    4
		--T;                // T = 1    5
	}
	return 0;
}