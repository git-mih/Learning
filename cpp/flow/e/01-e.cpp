#include <iostream>
using namespace std;

int main() {

    //program which will get x and y and print all numbers between x and y inclusive.
    //first try
    int start, end;
    cin>>start>>end; //test case: 5 9   -> output: 5, 6, 7, 8, 9

    if(end < start)  cout<<"invalid"<<"\n";
    else {
        while(start <= end){    // (5 <= 9) (6 <= 9) (7 <= 9) (8 <= 9) (9 <= 9) (10 <= 9)
            cout<<start<<"\n";  // print 5, 6, 7, 8, 9                            false
            start++; // 5 will become 6 
        }
    }

    return 0;
}