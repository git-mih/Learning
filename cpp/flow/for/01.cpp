#include<iostream>
using namespace std;
 
int main() {
	for (int a = 5; a > 1; a--, cout << a);   // a--, before the cout << a statement
        // a = 5       4        3      2
        // 5 > 1       4 > 1    3 > 1  2 > 1
        // a = 5 - 1   4 - 1    3 - 1  2 - 1
        // print 4       3        2      1
	return 0;
}