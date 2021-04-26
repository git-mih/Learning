#include <iostream>
using namespace std;

int main() {

    int a, b;
    char op;
    cout<<"Enter two numbers and a operation.: ";
    cin>>a>>op>>b; // 1 + 1

    if(op == '+') cout<<a + b<<"\n";
    if(op == '-') cout<<a - b<<"\n";
    if(op == '*') cout<<a + b<<"\n";
    if(op == '/') cout<<(double)a / (double)b<<"\n";

    return 0;
}