#include <iostream>
using namespace std;

int main () {
    // program which find the most frequent number inside an array of n integers (n <= 200)
    // we require to find the value that repeated the most number of times.
    // eg:  for array: 3    1 2 1 
    //           1 repeated 2 times

    int n, arr[200];

    cin >> n; // 3
    for (int i = 0; i < n; i++)  // i=0 <3
        cin >> arr[i]; // 1  2  1

    int max_value = -1, max_repeat = -1;

    for (int i = 0; i < n; i++) {      // i=0 <3 // i=1 <3
        // count how many times arr[i] exists
        int repeat = 0;

        for (int j = 0; j < n; j++) //                     i = 0                                              i = 1
            repeat += (arr[i] == arr[j]);   // repeat = 0 + (arr[i=0] == arr[j=0]) 1 == 1? y  // repeat = 0 + (arr[i=1] == arr[j=0]) 2 == 1? n
                                            // repeat = 1 + (arr[i=0] == arr[j=1]) 1 == 2? n  // repeat = 0 + (arr[i=1] == arr[j=1]) 2 == 2? y
                                            // repeat = 2 + (arr[i=0] == arr[j=2]) 1 == 1? y  // repeat = 1 + (arr[i=1] == arr[j=2]) 2 == 1? n

        if (max_repeat == -1 || max_repeat < repeat) { // max_repeat = -1        // max_repeat = 1, 1 < 1? n
            max_repeat = repeat;                       // max_repeat =  2        
            max_value = arr[i];                        // max_value = arr[0] = 1
        }
    }

    cout << max_value << " repeated " << max_repeat << " times";
    //         1                             2

    return 0;
}