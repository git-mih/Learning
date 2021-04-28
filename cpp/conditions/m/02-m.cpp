#include <iostream>
using namespace std;

int main()
{
    // program which will get a n integer and then read n integers and print the biggest value. (2 <= n <= 10)
    // if we pass (5) then we will read 5 more values and print the biggest. eg: (29 2 15 10 31) -> 31
    // if we pass (10) then read 10 more values and print the biggest
    int n, result;
    int counter;
    cin>>counter; // test case: 5  the counter will start with 5 and we require to decrease it

    cin>>result; // getting 1st number and storing into result.
    counter--; // counter = 4   we are going to ask for a value 4 more times

    if(counter > 0){
        cin>>n;    // getting 2nd number and then comparing with the value stored in the result
        if(n > result) // if value of 2nd number is bigger than value stored in the result, we replace the value 
            result = n;
        counter--; // counter = 3
    }

    // representing same code into a single line
    if(counter > 0)    {  cin>>n;   if(n > result)   result = n;   counter--;  } // counter = 2
    if(counter > 0)    {  cin>>n;   if(n > result)   result = n;   counter--;  } // counter = 1
    if(counter > 0)    {  cin>>n;   if(n > result)   result = n;   counter--;  } // we no longer ask new numbers
    if(counter > 0)    {  cin>>n;   if(n > result)   result = n;   counter--;  }
    if(counter > 0)    {  cin>>n;   if(n > result)   result = n;   counter--;  }
    if(counter > 0)    {  cin>>n;   if(n > result)   result = n;   counter--;  }
    if(counter > 0)    {  cin>>n;   if(n > result)   result = n;   counter--;  }
    if(counter > 0)    {  cin>>n;   if(n > result)   result = n;   counter--;  } // max 10 numbers we can ask to compare

    cout<<result;

    return 0;
}