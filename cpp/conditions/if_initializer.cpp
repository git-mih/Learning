#include <iostream>
using namespace std;

int main() {
    // we require to declare and initialize the variable outside the if statement to be able to perform a condition check.
    // we can declare and initialize a local variable to it, but it will be local to the block it was declared.
    int x = 11;
    if(x % 2 == 1) {
        cout<< x << " is odd\n"; // 11
        int a = 22; //avaiable only inside THIS if scope. Also static int a; would not work.
        cout<< a << " inner variable\n"; // 22

    } else if(x % 2 == 0)
        cout<< x << " is even\n";

    cout<< x <<" x variable outside scope of if\n"; //x variable was not local to the if statement above. we still can access it from here.

    /*
        C++ 17 we can initialize a variable directly inside the if statement
        it wont be avaiable outside the scope of the if/else block
    
    if(int y = 11; y % 2 == 1)      if(initialize ; condition) y will be avaiable inside if, else if, else blocks
        cout<< y << " is odd\n";
    else if(y % 2 == 0)
        cout<< y << " is even\n";
    */
    return 0;
}