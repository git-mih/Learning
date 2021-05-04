#include <iostream>
using namespace std;

int main(){
    // program which read a integer T for number of test cases
    // for each test case, read a integer N and then read N integers a, b, c, d ...
    //     a,  b*b,  c*c*c,  d*d*d*d,  ...
    // eg:
    //    input:  2   (3   5 7 2) (4   1 2 3 4)
    //    output: 62 288                       as 5 + 7*7 + 2*2*2
    //                                            1 + 2*2 + 3*3*3 + 4*4*4*4 

	/*
	   We need 3 nested loops
	   loop over test cases
	   	 loop over reading numbers
	   	   loop to repeat the number K times (multiplication)
	*/
	int T;
	cin >> T; // 2

	while (T > 0) { // (2 > 0)
		int N;
		cin >> N;   // 3

		int cnt_N = 1;
		int sum = 0;
		while (cnt_N <= N) { //       (1 <= 3)         (2 <= 3)     (3 <= 3)
			int value = 0; 
			cin >> value;  //            5                7             2

			int cnt_deep = cnt_N; // (cnt_deep = 1) (cnt_deep = 2)   (cnt_deep = 3)
			int result = 1;

			while (cnt_deep > 0) //                (1 > 0)            (2 > 0, 1 > 0)             (3 > 0, 2 > 0, 1 > 0)
				result *= value, cnt_deep--; // result = 1*5   result = 1*7 | result = 7*7    result = 1*2 | 2*2 |  2*2*2                          
                                       //       cnt_deep = 0       cnt_deep = 1   0

			sum += result; // sum = 0+5   sum = 5 + 49   sum = 5 + 49 + 2
			cnt_N++;      // cnt_N = 2     cnt_N = 3        cnt_N = 4
		}
		cout<<sum<<"\n"; // when T = 2   62 
		T--;             // when T = 1   288
	}
    return 0;
}
