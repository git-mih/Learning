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

    int i = 0;
    while(i < n){ // (0 < 4) (1 < 4) (2 < 4) (3 < 4) 
        cout<<ch; // will print the character Y, 4x 
        i++;
    }

    return 0;
}