#include <iostream>
using namespace std;

int main(){
    // program which read a integer T for a number of test cases
    // for each test case, read a integer N followed by reading N integers and then print the minimum value of the n integers
    // 1st try
    int T;  // test case: 2    im gonna read 2 test cases (6 3)
    cin>>T; // 2   6 (10 50 30 20 70 4) output: 4 is the minimum value in this case
            //     3 (10 5 30) output: 5 is the minimum

    int i = 1;
    while(i <= T){ // 1<=2  2<=2 and we will repeat all again 
        int lower = 0; // lower value needs to be 0 for every loop 
        int n;
        cin>>n; // 6  3                
        cin>>lower; // 10  ->  storing the 1st value of 6 numbers to be able to compare easily bellow
        while(n - 1 > 0){ //           5>0     4>0    3>0      2>0     1>0      n-1 cause we already got 1 of 6 integers
            int x = 0;
            cin>>x; // 50 // 30 // 20 // 70 // 4
            if(x < lower) // (50<10) (30<10) (20<10) (70<10) (30<10) (4<10)
                lower = x;//    F       F       F       F       F       T
            n--;     // lower = 10               ...                lower = 4
        }
        i++;
        cout<<"  "<<lower<<"\n"; // i = 1 output: 4
                                 // i = 2 output: 5
    }

    return 0;
}