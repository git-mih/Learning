#include <iostream>
using namespace std;

int main () {
    // fibonacci sequence
    int n;
    cin >> n; // test case: 6

    int a = 0, b = 1;

    cout << a << " " << b << " "; // 0 1

    for(int i=0; i < n; i++) { // 0<6   1<6         2<6         3<6         4<6         5<6
        int c = a + b; // c = 0+1  // c = 1+1  // c = 1+2  // c = 2+3  // c = 3+5  // c = 5+8
        a = b;         // a = 1    // a = 1    // a = 2    // a = 3    // a = 5    // a = 8
        b = c;         // b = 0+1  // b = 1+1  // b = 1+2  // b = 2+3  // b = 8    // b = 13

        cout << c << " "; // 1           2           3           5           8           13
    }
      //output:  0     1     1           2           3           5           8           13
      //         a     b     c           c           c           c           c           c
    return 0;
}