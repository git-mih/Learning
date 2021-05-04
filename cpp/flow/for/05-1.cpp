#include <iostream>
using namespace std;

int main () {
    // fibonacci sequence
    // another way
    int n;
    cin >> n; // test case: 6

    int i = 0; // initializing | cond | incrementing    
    for(int a = 0, b = 1, c = 0; i < n; c = a + b, a = b, b = c, i++) // 0<6 // 1<6 // 2<6 ...
        cout << a << " "; // output: 0  1  1  2  3  5  8
    return 0;         //         i = 0  1  2  3  4  5  6
}