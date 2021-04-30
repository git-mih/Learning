#include<iostream>
using namespace std;

int main() {   
    // another way
    // test case: 3  (10 20 30)   ->  output must be: (20 20) odd(10+30)/2 = 20, even(20)/1 = 2
	int n;
	cin >> n; // 3

	// using double to: allow any values and get average correctly
	double even_sum = 0, odd_sum = 0;
	int even_count = 0, odd_count = 0;

	int i = 1;
	while (i <= n) { // (1<=3) (2<=3) (3<=3)
		double value;
		cin >> value; // (10) (20) (30)

		if (i % 2 == 0)	// (1%2 == 1) (2%2 == 0) (3%2 == 1)
			even_sum += value, even_count++; // (even_sum = 0+20 and even_count = 1)
		else
			odd_sum += value, odd_count++; // (odd_sum = 0+10 and odd_count = 1) (odd_sum = 10+30 and odd_count = 2)

		i++;
	}

	cout <<odd_sum / odd_count << " " << even_sum / even_count << "\n";
    //          40 / 2                         20 / 1
    //            20                             20

	return 0;
}

