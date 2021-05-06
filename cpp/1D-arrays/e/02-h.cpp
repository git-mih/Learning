#include <iostream>
using namespace std;

int main () {
    int n, arr[200];

    int lower, higher;

    cin >> n;
    for (int i = 0; i < n; i++) 
        cin >> arr[i];

    // getting lower and higher
    for (int i = 0; i < n; i++) {
        if (i == 0)
            lower = arr[i];
        else if (arr[i] < lower)
            lower = arr[i];

        for (int j = 0; j < n; j++) {
            if (j == 0)
                higher = arr[j];
            else if (arr[j] > higher)
                higher = arr[j];
        }
    }

    // swapping all Min-Max values
    for (int i = 0; i < n; i++) { 
        if (lower == arr[i]) {  // lower = arr[1]= 1  == arr[0]= 4  false
            arr[i] = higher;    // lower = arr[1]= 1  == arr[1]= 1  True,  then we swap the arr[1] to be the Max value
        }
        else if (higher == arr[i]) 
            arr[i] = lower;
    }

    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";

    return 0;
}