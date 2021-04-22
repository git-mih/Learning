#include <iostream>
using namespace std;
int main(){

    // a program that reads integer N and Print the sum from 1 to N
    int n;
    cout<<"enter value: ";
    cin>>n;

    cout<<(n*(n+1))/2;
    /*
    n = 6    -> 1 + 2 + 3 + 4 + 5 + 6
                1+6, 2+5, 3+4  ->  first number and last number, 2nd number, and 2nd from back...
    7 = n+1  ->  7    7    7
    3 = n/2  -> number of pairs 

      n(n+1)
     --------
        2
    */
    return 0;
}