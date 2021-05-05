#include <iostream>
using namespace std;

int main () { 
    // program which read a integer n, then read n numbers. (n <= 200)
    // and print the reverse order by using only one array.
    // eg:   input:   5     1 2 3 4 5  // output: 5 4 3 2 1
    //        read 5 int    a b c d e

    int n, arr[200];
    cin >> n;

    for (int i = 0; i < n; i++)
        cin >> arr[i];

    for (int i = 0; i < n/2; i++) {
        int last = n - i - 1;

        int temp = arr[i];  // temp = arr[0] = 1    // temp = arr[1] = 2
        arr[i] = arr[last]; // arr[0] = arr[4] = 5  // arr[1] = arr[3] = 4
        arr[last] = temp;   // arr[4] = temp = 1    // arr[3] = temp = 2
    }

    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";

    return 0;
}   