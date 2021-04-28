#include <iostream>
using namespace std;

int main()
{
    int a,b;
    cin>>a>>b; // test cases: (5 7)  (12 2)  (5 6)  (12 3)

    if(a % 2 != 0 && b % 2 != 0) // both odd -> a * b
        cout<< a * b<<"\n";
    else if(a % 2 == 0 && b % 2 == 0) // both even -> a / b
        cout<< a / (double)b<<"\n";
    else if(a % 2 != 0 && b % 2 == 0) // 1st odd and 2nd even -> a + b
        cout<< a + b<<"\n";
    else  // 1st even and 2nd odd -> a - b
        cout<< a - b<<"\n";
    return 0;
}