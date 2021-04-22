#include <iostream>
using namespace std;

int main(){

    int a,b,c,x = -1;
    cin>>a>>b>>c;
    x = a; //temporary storage
    b = c;
    c = x;
    cout<<a<<" "<<b<<" "<<c<<"\n";
    return 0;
}