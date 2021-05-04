#include <iostream>
using namespace std;

int main() {
    // variable declaration inside loop
    int x = 0;
    printf("%d ", &x); // 6422296
    printf("%d ", x);  // 0
    cout<<"\n";

    int i = 0;
    while(i < 5){
        int x = 1; // by creating variables inside loops, we ensure their scope is restricted to inside the loop.
                   // it cannot be referenced nor called outside of the loop.
                   // Also, the variable is allocated once, when the function is called. The compiler wont allocate it again for each loop
        printf("%d ", &x); // 6422292
        printf("%d ", x);  // 1
        cout<<"\n";
        i++;
    }

    printf("%d ", &x); // 6422296 
    printf("%d ", x);  // 0
    cout<<"\n";

    return 0;
}