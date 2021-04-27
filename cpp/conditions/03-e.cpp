#include <iostream>
using namespace std;

int main()
{
    // program which get 3 integers and find the biggest one of them which is < 100.
	int a, b, c;
	cin>>a>>b>>c;  // test case: (22 90 115) (200 300 115) (50 100 150) (10 30 20)
                   // output:        90           -1            50          30
	int result = -1;

    //assuming given input is (22 90 115)

	if (a < 100 && a > result) //yep
		result = a; // result = 22

	if (b < 100 && b > result) //yep
		result = b; // result = 90

	if (c < 100 && c > result) //nop
		result = c;

	cout<<result<<"\n"; // 90

    return 0;
}