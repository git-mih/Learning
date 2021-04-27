#include <iostream>
using namespace std;

int main()
{
    //program which read number X and other 5 numbers and then print 2 values:
    //  1. how many numbers are <= X
    //  2. how many numbers are > X
   
    int X, num1,num2,num3,num4,num5;
    cin>>X>>num1>>num2>>num3>>num4>>num5; // 10   7 2 50 90 4 

    int output_lesser = 0;
    int output_higher = 0;

    if(num1 <= X)
        output_lesser++; 
    else
        output_higher++;
    
    if(num2 <= X)
        output_lesser++; 
    else
        output_higher++;
    
    if(num3 <= X)
        output_lesser++; 
    else
        output_higher++;
    
    if(num4 <= X)
        output_lesser++; 
    else
        output_higher++;
    
    if(num5 <= X)
        output_lesser++; 
    else
        output_higher++;
    
    cout<<output_lesser<<" "<<output_higher<<"\n";

    return 0;
}