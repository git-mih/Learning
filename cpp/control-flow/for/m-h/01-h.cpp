#include <iostream>
using namespace std;

int main () {
    /*
    star pattern
        *   *
         * *
          *
         * *
        *   *
    */
    // 1st try
    int n;
    cin >> n; // test case = 4

    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= n; j++) {
            if (j == i)  
                cout << "*"; 
            else if (j == n-i) 
                cout << "*";
            else
                cout << " ";
        }
        cout << "\n";
    }
    return 0;
}