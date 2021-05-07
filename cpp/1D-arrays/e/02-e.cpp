#include <iostream>
using namespace std;

int main () {
    // program which read a integer n (n <= 200). then read n integers.
    // print the array after doing the following operations:
    // 		find the minimum number in the array
	// 		find the maximum number in the array
	// 		then replace each min number with the max number and vice versa.
	// eg: 
	//     input: 7   4  1  3  10  8  10  10       // 10 is the max and 1 is the min number
	// 	   output:    4  10 3  1   8  1   1   
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