#include <iostream>
using namespace std;

int main() {
    // 1st try
    //program which will get a integer x and 6 numbers and print how many times x exist inside those intervals
    // test case: 7 [1 10] [5 6] [4 20]
    //                +1     0     +1     7 exists in 2 intervals [1 10] and [4 20] but not in [5 6]

    int x; // 7
    int s1,e1; // [1 10]  
    int s2,e2; // [5 6] 
    int s3,e3; // [4 20] 

    cin>>x;
    cin>>s1>>e1>>s2>>e2>>s3>>e3;

    int result = 0; // gonna count how many times the x value will exist inside those 3 intervals 

    if(s1 <= x && x <= e1) result++; // +1
    if(s2 <= x && x <= e2) result++;
    if(s3 <= x && x <= e3) result++; // +1

    cout<<result; // 2

    return 0;
}