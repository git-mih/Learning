#include <iostream>
using namespace std;

int main () {
    // program which read a integer n, then print its reverse integer R and R*3
    // input:  123
    // output: 321 963
    // 1st try

    int n; // test case: 123
    cin >> n; 
    int n_copy = n; // storing n no perform the inverse (R*3) later

    while (n) {  //    123    12    1
        int R = n % 10; // R=3 R=2 R=1
        cout << R; // 321
        n /= 10; // n=12 n=1 n=0
    }
    cout << " ";

    while (n_copy) { // 123   12   1
        int R = n_copy % 10; // 3  2  1
        cout << R*3;  // 963
        n_copy /= 10;  // n_copy=12  n_copy=1
    }

    return 0;
}