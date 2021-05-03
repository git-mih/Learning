#include <iostream>
using namespace std;

int main(){
    // program which will read a integer N and print all numbers that satisfy the following:
    // either number is divisible by 8 or divisible by both 4 and 3
    // 1st try
    int n;
    cin>>n; // test case 100     (0 8 12 16 24 32 36 40 48 56 60 64 72 80 84 88 96)

    int i = 0;
    while(i < n){
        if(i % 4 == 0 && i % 3 == 0){ // i could also specify all together:
            cout<<i<<" ";             // if(i % 8 == 0 || i % 4 == 0 && i % 3 == 0) cout<< i <<" ";
        } else if(i % 8 == 0){
            cout<<i<<" ";
        }
        i++;
    }

    return 0;
}