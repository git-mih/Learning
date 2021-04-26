#include <iostream>
using namespace std;

int main(){
    // program which print the minimum value of 3 given numbers.
    int a,b,c;
    cin>>a>>b>>c;

    int result = a; // easily scalable aproach

    if(result > b)
        result = b;
    if(result > c)
        result = c;

    cout<<result<<"\n";

    /*  
    my 1st try not scalable...
    
    if(a < b && a < c)
        cout<<a<<"\n";
    else if(b < a && b < c)
        cout<<b<<"\n";
    else
        cout<<c<<"\n";
    */

    return 0;
}