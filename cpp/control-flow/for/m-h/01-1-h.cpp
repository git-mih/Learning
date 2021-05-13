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
    // fixing my 1st try
    int n;
    cin >> n; // test case = 5

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) { //        n i             n i             n i             n i
            if (j == i || j == n-i-1) // j=0 == 4-0-1 // j=1 == 4-0-1 // j=2 == 4-0-1 // j=3 == 4-0-1
                cout << "*";    //         0 == 3          1 == 3          2 == 3          3 == 3
            else                //           0               0               0               *
                cout << " ";    //       j=0 == 4-1-1 // j=1 == 4-1-1 // j=2 == 4-1-1
        }                       //         0 == 2          1 == 2          2 == 2       
        cout << "\n";           //           0               0               *
    }                           //       j=0 == 4-2-1 // j=1 == 4-2-1
                                //         0 == 1          1 == 1           
    return 0;                   //           0               *
}                               //       j=0 == 4-1-1
                                //         0 == 0                     
                                //           *