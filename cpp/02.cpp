#include <iostream>
#include <climits>
using namespace std;

int main(){

    // program which will count the number of digits of a given number
    // to count number of digits divide the given number by 10 till number
    // is greater than 0. for each iteration, we increment the value of digits_count variable.

    long long num; // im using long data type to avoid the integer overflow. otherwise, i would not be able to handle +10 digits number
    cin>>num; // 1234

    int digits_count = 0;

    /*
    if(num == 0) // if i dont specify it, i cant make the while condition true (0 > 0) and the output would be 0 
        digits_count = 1;
    else {if(num < 0) num = num * -1;} // -1234 * (-1) = 1234
    */

    while(num > 0){     // (1234 > 0) (123 > 0) (12 > 0) (1 > 0) (0 > 0)
        digits_count++;//      0          1         2        3       
        num /= 10;    // 1234 will become 123, 12, 1 and finally 0
    }

    cout<<digits_count<<"\n"; // 4

    return 0;
}