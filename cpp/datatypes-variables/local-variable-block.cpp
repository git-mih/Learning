#include<iostream>
using namespace std;

int main() {
    // creating a block of code
    {
        int x = 0;  // x will be avaiable only between {}
        printf("%d ", &x); // 6422292
        printf("%d ", x);  // 0
        cout<<"\n";

        if(1 < 2)
            cout<<x; // 0
    }

    // cout << x;    // error: 'x' was not declared in this scope
    // x wont be avaiable outside the scope above

	return 0;
}