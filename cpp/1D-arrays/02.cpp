#include <iostream>
using namespace std;

int main () {
    // program which read a integer n, then read n (distinct) numbers.
    // and find a pair of numbers whose sum is maximum.
    // eg:  input:  5    2 10 3 50 15  // output: 65 (from 50 + 15)
    //       read 5 int  a b  c d  e
    // 1st try
    int n, arr[200];
    cin >> n;

    int max1, max2;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];

        if (i == 0) 
            max1 = arr[i]; 
        else if (i == 1) 
            max2 = arr[i]; 

        if (arr[i] > max1)      
            max1 = arr[i];      
        else if (arr[i] > max2) 
            max2 = arr[i];
    }

    int result = max1 + max2;

    cout << result;

    return 0;
}