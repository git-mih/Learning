#include<iostream>
using namespace std;

int main() { 
    // program which read a integer n and m, then print n*m lines for their multiplication table.
    // input: 2 4
    /* eg:
           1*1   2*1
           1*2   2*2
           1*3   2*3
           1*4   2*4
    */
	int n, m;
	cin >> n >> m; // test case: 2 4

	int cnt_n = 1;

	while (cnt_n <= n) {  // (1<=2)
		int cnt_m = 1; 

		while (cnt_m <= m) {  // (1<=4) (2<=4) (3<=4) (4<=4)                                  cnt_n = 1                 cnt_n = 2
			cout << cnt_n << " x " << cnt_m << " = " << cnt_n * cnt_m << "\n"; // (1x1=1) (1x2=2) (1x3=3) (1x4=4) | (2x1=2) (2x2=4) ...
			cnt_m++; // cnt_m = 2 3 4
		}
		cnt_n++; // ctn_n = 2
	}
	return 0;
}

