#include <iostream>
using namespace std;

int main() {
    // program which get 2 values and perform some operation based on input
    int a, b; // 1  3
    char op;  // '+'
    cout<<"Enter two numbers and a operation: "; // 1 + 3
    cin>>a>>op>>b;

    if(op == '+') 
        cout<<a + b<<"\n"; // 4
    if(op == '-') 
        cout<<a - b<<"\n"; 
    if(op == '*') 
        cout<<a + b<<"\n";
    if(op == '/') 
        cout<<(double)a / (double)b<<"\n";

    return 0;
}
