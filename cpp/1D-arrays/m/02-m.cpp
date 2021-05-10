#include <iostream>
using namespace std;

int main () {
    // program which read an integer n and then read n numbers.
    // then we require to read a integer q (for a number of queries), then read q integer (the query numbers we want to search for)
    //      for each integer, find the last occurance in the array and print its Index.
    //      and if it doesnt exists, print -1
    // eg: input: 5    1 2 7 3 7      3   7 9 2    reading 3 queries
    //                         output:    4 -1 1   (7 last index is [4], 9 doesnt exist, 2 is in a[1])
    // 1st try

    int n, a[200];
    cin >> n;

    for (int i = 0; i < n; i++)
        cin >> a[i];

    int number_of_queries;
    cin >> number_of_queries;

    while (number_of_queries--) {
        int query;
        cin >> query;

        int output = -1; // if the query number doesnt have inside the array, we are not going to reasign this variable

        for (int i = n - 1; i >= 0; i--) {
            if (query == a[i]) {
                output = i;
                break; // to stop looping and prevent printing 7 more than once
            }
        }

        cout << output << " ";
    }

    return 0;
}