#include <iostream>
using namespace std;

int main(){
    // program which read a integer and if the number is odd, it will check the length and print 
    // the last 2 or 3 digits. And if the number is evend, it will print only the last digit
    int num;
    cin>>num;

    if(num % 2 != 0){ // odd
        if(num < 1000)
            cout<<num % 100<<"\n"; // last 2
        else if(num < 1000000)
            cout<<num % 1000<<"\n"; // last 3
        else
            cout<<-num<<"\n";
    } else // even
        cout<<num % 10<<"\n"; // last

    return 0;
}