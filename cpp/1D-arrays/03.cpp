#include <iostream>
using namespace std;

int main () {
    // program which read a integer n, then read n numbers. (n <= 200)
    // and print the reverse order by using only one array.
    // eg:   input:   5     1 2 3 4 5  // output: 5 4 3 2 1
    //        read 5 int    a b c d e

    int n, arr[200];
    cin >> n; // 5

    int temp_1st;  // 1
    int temp;

    for (int i = 0; i < n; i++)  
        cin >> arr[i]; 
    
    for (int i = 0; i < n/2; i++) { // n/2 = 2   (0<2) (1<2)

        if (i == 0)
            temp_1st = arr[i]; // temp_1st will store the value of 1st element value of the array which is 1    arr[0] = 1
        else 
            temp = arr[i];    // i != 0 will store inside temp   arr[1] = 2
    
        //as long as we stored the arr[0] value in temp_1st, we can replace it now    
        arr[i] = arr[n-i-1];  // replacing arr[0] with the last element value which is 5     arr[0] = int 5 

        if (i == 0)
            arr[n-i-1] = temp_1st; // placing 1st element in the last index     arr[4] = 1
        else
            arr[n-i-1] = temp;  // arr[3] = 2 // arr[2] = 3 ...
    }

    for (int i = 0; i < n; i++)
        cout << arr[i] << " "; 

    return 0;
}