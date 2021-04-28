#include <iostream>
using namespace std;

int main()
{
    //program which get 3 values and sort in ascending order and print them
    int a,b,c;
    cin>>a>>b>>c; //output must be (1 2 3) to any given input such as (2 3 1) (3 2 1) (3 1 2) etc...

    if(a < b && a < c) // a lesser than b and c
        if(b < c)
            cout<<a<<" "<<b<<" "<<c<<"\n";
        else
            cout<<a<<" "<<c<<" "<<b<<"\n";

    if(b < a && b < c) // b lesser than a and c
        if(a < c)
            cout<<b<<" "<<a<<" "<<c<<"\n";
        else 
            cout<<b<<" "<<c<<" "<<a<<"\n";

    if(c < a && c < b) // c lesser than a and b
        if(a < b)
            cout<<c<<" "<<a<<" "<<b<<"\n";
        else
            cout<<c<<" "<<b<<" "<<a<<"\n";

    return 0;
}