#include <iostream>
using namespace std;

int main () {
    // program which find the most frequent number inside an array of n integers (n <= 200)
    // we require to find the value that repeated the most number of times.
    // eg:  for array: 7    1 2 1 2 2 3 2 
    //           2 repeated 4 times

    // Another way by using a trick called Frequency Array 
    
    int n, arr[200];

    int frequency[150+1] = {0}; // set all 0

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        frequency[arr[i]]++;
    }

    int max_pos = -1;

    for(int i = 0; i < 151; i++) { // iterate on ALL array
        if (max_pos == -1 || frequency[max_pos] < frequency[i])
            max_pos = i;
    }

    cout << max_pos << " repeated " << frequency[max_pos] << " times";

    return 0;
}