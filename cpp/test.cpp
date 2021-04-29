#include <iostream>
using namespace std;

int main(){

    //program which will count the number of digits of a given integer
    int num;
    cin>>num; // 1234

    int digits = 0;

    while(num > 0){ // (1234 > 0) (123 > 0) (12 > 0) (1 > 0) (0 > 0)
        digits++;   //     0          1         2        3       
        num /= 10;  // 1234 will became 123, 12, 1 and finally 0
    }

    cout<<digits<<"\n";

    return 0;
}