#include <iostream>
using namespace std;

int main(){
    // program which read a integer n and print the first n numbers that are:
    // multiple of 3 but not multiple of 4
    // 1st try
    int n; // test case: 11    output = (3 6 9 15 18 21 27 30 33 39 42)
    cin >> n;

    int i = 0;
    while(i < n){ // (0 < 11) (1 < 12) (2 < 13) (3 < 14)
        if(i % 3 == 0 && i % 4 != 0){ // (0%3==0 && 0%4!=0) (1%3==0 && 1%4!=0) (2%3==0 && 2%4!=0) (3%3==0 && 3%4!=0) ...
            cout<<i<<" ";             //     T      F           F      T           F       T        ** T       T ***
        }else{                     // output: 3
            n++; // n = 12 // n=13 // n=14 whenever we are able to print, n value wont be incremented. now we keep doing it to print all 10 remaining values (6 9 15 18 21 27 30 33 39 42)
        }
        i++; // i = 1 // i=2 // i=3 // i=4 ...
    }

    return 0;
}