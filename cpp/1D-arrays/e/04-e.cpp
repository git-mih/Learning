#include <iostream>
using namespace std;

int main () {
    // program which read a integer n (n < 1000), then read n integer of an array.
    // determine if the array is Palindrome or not.
    //      an array is called palindrome if it reads the same backward and forward
    //      then print YES or NO.
    //
    // eg:  input:  5    1 2 3 2 1   output: YES
    //                   1 3 2 3 1   output: YES
    //      input:  4    1 2 3 4     output: NO
    // 1st try

    int n, arr[1000];

    string result;

    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    
    for (int i = 0, j = n-1; i <= n/2; i++, j--) {     
        if (arr[i] != arr[j]) {
            result = "NO";
            break;
        } else {
            result = "YES";
        }
    }

    cout << result;

    return 0;
}