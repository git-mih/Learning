#include <iostream>
using namespace std;

int main()
{
    //  better version of the previous program which read number X and other 5 numbers and then print 2 values:
    //  1. how many numbers are <= X
    //  2. how many numbers are > X

	int x, a1, a2, a3, a4, a5;
	cin>>x>>a1>>a2>>a3>>a4>>a5; // assuming the values (10   7 2 50 90 4 )

	int cnt = 0;
                      // either 1 or 0   if its true, then 1 will be added to cnt
	cnt += (a1 <= x); // 7 <= 10   cnt = 1
	cnt += (a2 <= x); // 2 <= 10   cnt = 1 + 1 
	cnt += (a3 <= x); // 50 > 10   cnt = 1 + 1 + 0 
	cnt += (a4 <= x); // 90 > 10   cnt = 1 + 1 + 0 + 0 
	cnt += (a5 <= x); // 4 <= 10   cnt = 1 + 1 + 0 + 0 + 1   cnt = 3  (number of values <= X)

	cout <<cnt<<" "<< 5 - cnt<<"\n"; // 3 2
    //    <= X          > X
    //      3            2

    // relationship between numbers (<= X) and (> X) is 5 - cnt

    return 0;
}