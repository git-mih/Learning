#include <iostream>
using namespace std;

int main () {
    // program which read a integer n, then read n (distinct) numbers.
    // and then find the maximum and 2nd maximum values.
    // eg:   input:    5    10 20 3 30 7 //  output: 30 20
    //        read 5 int -> a  b  c  d e 
    // 1st try
    int n;
    cin >> n;

    int arr[n] {};

    int max, max2;

    for (int i = 0; i < n; i++) {

        cin >> arr[i];

        if (i == 0) {
            max = arr[i];
            continue;
        }
        else if (i == 1) {
            max2 = arr[i];
            continue;
        }

        if (arr[i] > max)
            max = arr[i];
        else if (arr[i] > max2)
            max = arr[i];
    }

    if (max > max2)
        cout << max << " " << max2 << "\n";
    else
        cout << max2 << " " << max << "\n";

    return 0;
}