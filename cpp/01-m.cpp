#include <iostream>
using namespace std;

int main()
{
    // program which read 10 values and print the biggest value
    // my first try
    int a1,a2,a3,a4,a5,a6,a7,a8,a9,a10;
    cin>>a1>>a2>>a3>>a4>>a5>>a6>>a7>>a8>>a9>>a10;

    int result;
    if(a1 > a2 && a1 > a3 && a1 > a4 && a1 > a5 && a1 > a6 && a1 > a7 && a1 > a8 && a1 > a9 && a1 > a10)
        result = a1;
    if(a2 > a1 && a2 > a3 && a2 > a4 && a2 > a5 && a2 > a6 && a2 > a7 && a2 > a8 && a2 > a9 && a2 > a10)
        result = a2;
    if(a3 > a1 && a3 > a2 && a3 > a4 && a3 > a5 && a3 > a6 && a3 > a7 && a3 > a8 && a3 > a9 && a3 > a10)
        result = a3;
    if(a4 > a1 && a4 > a2 && a4 > a3 && a4 > a5 && a4 > a6 && a4 > a7 && a4 > a8 && a4 > a9 && a4 > a10)
        result = a4;
    if(a5 > a1 && a5 > a2 && a5 > a3 && a5 > a4 && a5 > a6 && a5 > a7 && a5 > a8 && a5 > a9 && a5 > a10)
        result = a5;
    if(a6 > a1 && a6 > a2 && a6 > a3 && a6 > a4 && a6 > a5 && a6 > a7 && a6 > a8 && a6 > a9 && a6 > a10)
        result = a6;
    if(a7 > a1 && a7 > a2 && a7 > a3 && a7 > a4 && a7 > a5 && a7 > a6 && a7 > a8 && a7 > a9 && a7 > a10)
        result = a7;
    if(a8 > a1 && a8 > a2 && a8 > a3 && a8 > a4 && a8 > a5 && a8 > a6 && a8 > a7 && a8 > a9 && a8 > a10)
        result = a8;
    if(a9 > a1 && a9 > a2 && a9 > a3 && a9 > a4 && a9 > a5 && a9 > a6 && a9 > a7 && a9 > a8 && a9 > a10)
        result = a9;
    if(a10 > a1 && a10 > a2 && a10 > a3 && a10 > a4 && a10 > a5 && a10 > a6 && a10 > a7 && a10 > a8 && a10 > a9)
        result = a10;
    
    cout<<result<<"\n";
    return 0;
}