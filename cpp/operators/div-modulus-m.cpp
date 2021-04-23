#include <iostream>
using namespace std;

int main(){
    // 3 different ways to know if a given number is even or not
    int num;
    cout<<"Enter a number: "; // try 10 or 11
    cin>>num;

	// Is even using %2
	bool is_even1 = (num % 2 == 0);

	// is even using /2
	double by2 = (double)num / 2.0; // this is either x.0 or x.5
	by2 = by2 - (int)by2; // now we remove the integer part (x) and this is now either 0 (for even) or 0.5 (for odd)
	bool is_even2 = by2 == 0;

	// is even using %10
	int last_digit = num % 10; // to get even, the last digit need to be 0, 2, 4, 6, 8
	bool is_even3 = last_digit == 0 || last_digit == 2 || last_digit == 4 || last_digit == 6 || last_digit == 8;

    cout<<is_even1<<" "<<is_even2<<" "<<is_even3<<"\n";

    cout<<"---------------------\n";

    // program that reads an integer and prints the sum of the last 3 digits
    int num2; //try 1234   -> 2 + 3 + 4 = 9
    cin>>num2;
    int last1 = num2 % 10; //4
    int last2 = (num2 % 100)/10; //34 / 10 = 3
    int last3 = (num2 % 1000)/100; //234 / 100 = 2

    int result = last1 + last2 + last3; //9
    cout<<result<<"\n";

    cout<<"---------------------\n";

    // program that reads an integer and print the 4th last digit, and 0 if there is no 4th last digit
    int num3;
    cin>>num3; //try 12345

    int fourth_last_digit = (num3/1000)%10; // /1000 removes the last 3 digits(345) and %10 get the next digit (4th last = 2)
    //       or  ->         (num%10000)/1000 

    cout<<fourth_last_digit<<"\n"; // 2

    return 0;
}