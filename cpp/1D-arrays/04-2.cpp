#include <iostream>
using namespace std;

int main () {
    // program which find the most frequent number inside an array of n integers (n <= 200)
    // we require to find the value that repeated the most number of times.
    // eg:  for array: 7    1 2 1 2 2 3 2 
    //           1 repeated 2 times
    //           2 repeated 2 times
    //           3 repeated 1 times

    // Another way by using a trick called Frequency Array 

    int counter = 0;
    int a[200], b[200];

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) 
        cin >> a[i];
    
    for (int i = 0; i < n; i++) {
        counter = 1;
        if (a[i] != -1) {
            for (int j = i + 1; j < n; j++) {
                if (a[i] == a[j]) {
                    counter++;
                    a[j] = -1;
                }
            }

        b[i] = counter; // b is storing the counters value for each iteration.

        }
    }

    for (int i = 0; i < n; i++) {
        if (a[i] != -1) 
            cout << a[i] << " repeated " << b[i] << " times" << "\n"; // a[0] contains b[0] times  // a[1] contains b[1] times ...
    }                                                                 //  #1    counters: 2        //  #2    counters: 4       ...

    return 0;
}