#include<iostream>
using namespace std;
 
int main() {
    // program which read a integer T for number of test cases
    // for each test case, read a integer N and then read N integers a, b, c, d ...
    //     a,  b*b,  c*c*c,  d*d*d*d,  ...
    // eg:
    //    input:  2   (3   5 7 2) (4   1 2 3 4)
    //    output: 62 288                       as 5 + 7*7 + 2*2*2
    //                                            1 + 2*2 + 3*3*3 + 4*4*4*4 
    int N, value;

    int T;
    cin >> T;
    while (T--) { // 1
        cin >> N; // 3

        int sum = 0;
        for (int i = 0; i < N; i++) { // 0 < 3 // 1 < 3 // 2 < 3
            cin >> value; //               5        7        2

            int result = 1;
            for (int j = 0; j <= i; j++) { // 0 < 0 // 0 <= 1  1 <= 1 // 0 <= 2  1 <= 2  2 <= 2
                result *= value; // result = 1*5 // result = 1*7*7 // result = 1*2*2*2
            }
            sum += result; // sum = 0 + 5 // sum = 5 + 49 // sum = 54 + 8
        }
        cout << sum << " " << "\n"; // 62
    }
	return 0;
}