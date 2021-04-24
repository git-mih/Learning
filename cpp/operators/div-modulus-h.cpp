#include <iostream>
using namespace std;

int main(){
    // a program which prints 100 if given number is even, or 7 if number is odd. by using pure math
	int n;
	cin >> n;

	int is_even = n % 2 == 0; // condition which will return true or false, 1 or 0
	int is_odd = 1 - is_even; // if is_even = 1, is_odd will be 0. 
                              // if is_even = 0, is_odd will be 1

	// formula of 2 parts: only one of them will be activated
	int result = is_even * 100 + is_odd * 7;
    //                 1*100   +   0*7      or      0*100   +   1*7
    //                  100    +    0                 0     +    7
    //                        100                           7
    //                    if is even                    if is odd

	cout<<result<<"\n";

    cout<<"--------------\n";


    return 0;
}