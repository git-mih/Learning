#include<iostream>
using namespace std;

int main() {   
    //better version
    //program which will get a integer x and 6 numbers and print how many times x exist inside those intervals
    // test case: 7 [1 10] [5 6] [4 20
	int x, start, end, cnt = 0;

	cin>>x;

	//read start and end, then see if x is between them or not, 3 times
	cin>>start>>end;
	cnt += (start <= x && x <= end); // +1    either 1 or 0. then it will add into cnt

	cin>>start>>end;
	cnt += (start <= x && x <= end); // +0

	cin>>start>>end;
	cnt += (start <= x && x <= end); // +1

	cout<<cnt<<"\n"; // 2

	return 0;
}

