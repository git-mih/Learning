#include <iostream>
using namespace std;

int main() {

    //program which will get a integer n and a character, then will print the character n times
    //first try
    //test case: 4 Y
    int n;
    cin>>n; //n = 4
    char ch;
    cin>>ch; //ch = Y    output: YYYY

    while(n > 0){ // (4>0) (3>0) (2>0) (1>0) 
        cout<<ch; // will print the character Y, 4x 
        n--;
    }

    return 0;
}