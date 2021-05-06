#include <iostream>
using namespace std;

int main () {
    // program which will read a integer n (<= 200), then read n integers and print YES or NO
    //      if the element order of the array is increasing, then print YES, otherwise print NO.
    //          input:  4   1 2 3 4  // output: YES
    //                  5   1 0 7 8 9 // output: NO
    // 1st try

    int n, arr[200];

    string result;
    int temp = -1;

    cin >> n;  
    for (int i = 0; i < n; i++) {    
        cin >> arr[i];  

        if (i == 0) {  
            temp = arr[i]; // storing 1st element 
            continue;
        }
        else if (arr[i] < arr[0]) { // cheking if 2nd element is greater than 1st one
                result = "NO";
                break;
        }

        // cheking remaining elements one by one 
        else {
            if (arr[i] >= temp) { 
                result = "YES";   
                temp = arr[i];    
            } else {
                result = "NO";  
                break;
            }
        }
    }

    cout << result << "\n";

    return 0;
}