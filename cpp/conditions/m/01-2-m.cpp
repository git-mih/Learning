#include <iostream>
using namespace std;

int main()
{    
    // program which read 10 values and print the biggest value by using 2 integers only

    int result, n;

    cin>>result; // getting 1st number and storing into result.
                 // now we ask again and again for numbers and keep comparing with the result

    cin>>n;      // asking 2nd number and comparing if this one is bigger than the value stored in result
    if(n > result)  // if 2nd number is bigger, then we replace the result with this new value
        result = n;

    cin>>n;    if(n > result)    result = n; // same code above into a single line x8 (readability)
    cin>>n;    if(n > result)    result = n;
    cin>>n;    if(n > result)    result = n;
    cin>>n;    if(n > result)    result = n;
    cin>>n;    if(n > result)    result = n;
    cin>>n;    if(n > result)    result = n;
    cin>>n;    if(n > result)    result = n;
    cin>>n;    if(n > result)    result = n;

    cout<<result<<"\n"; 
    
    return 0;
}