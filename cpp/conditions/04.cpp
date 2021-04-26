#include <iostream>
using namespace std;

int main() {
    // program which read a integer number and perform the sum of the last 3 values if the number is > 10000
    // and if the sum of the last 3 values are even, we check if we have odd number in there.
    // the output is based on it
    int n, last1, last2, last3;
    int sum;
    cin>>n;

    if(n < 10000)
        cout<<"Its a small number\n";
    else   // n = 12345
    {              
        last1 = n % 10;  // 5
        n /= 10;         // n = 1234
        last2 = n % 10;  // 4
        n /= 10;         // n = 123
        last3 = n % 10;  // 3  Old value of n is gone...

        sum = last1 + last2 + last3; // 5+4+3 = 12

        if(sum % 2 == 0) { // sum of last 3 digits are even (5+4+3 = 12)
            if(last1 % 2 != 0 || last2 % 2 != 0 || last3 % 2 != 0){ //checking the odd numbers present in the sum
                cout<<"Its a good number\n"; // 5 or 3 of (5+4+3) are odd number
            } else {
                cout<<"Its a bad number\n"; // case of being even and having any odd values, eg: 10000 (0+0+0) 
            }
        } else { 
            cout<<"Its a great number\n"; // comes here if the sum of last 3 digits are odd value
          }
    }
    return 0;
}