#include <iostream>
using namespace std;

int main () {
    // program which read a integer n, then read n (distinct) numbers.
    // and then find the maximum and 2nd maximum values.
    // eg:   input:    5    10 20 3 30 7 //  output: 30 20
    //        read 5 int -> a  b  c  d e 
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

    if (max1 > max2)
        cout << max1 << " " << max2 << "\n";
    else
        cout << max2 << " " << max1 << "\n";

    return 0;
}