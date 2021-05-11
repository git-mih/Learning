#include <iostream>
using namespace std;

int main () {
    // digit frequency program.
    // for all digits from 0 to 9, we want to know how many times it appeared
    // test case: 78 307     
    // 1st try

    int n {10}, arr[10] {0,1,2,3,4,5,6,7,8,9}, frequency[n] {0};

    int value;
    cout << "enter a number: ";
    cin >> value; // 78

    for (int i = 0; i < n; i++) {
        if (value == 0)
            break;

        int digit {value % 10}; // digit = 8
        value /= 10; // 7

        for (int j = 0; j < n; j++) {
            if (arr[j] == digit)
                frequency[j]++;
        }
    }

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " " << frequency[i] << "\n";
    }
    return 0;
}   