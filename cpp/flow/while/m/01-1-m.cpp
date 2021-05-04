#include <iostream>
using namespace std;

int main(){
    // diamond pattern
    // 2nd try
    int n;
    cin>>n; // test case: 5

    int i = 1;
    while(i <= n){
        int k = n; // spaces  5
        while(k - 1 >= i){ // 4 >= 1 // 3 >= 1// 2>= 1 // 1 >= 1 ||| 4 >= 2 // 3 >= 2 // 2 >= 2 ||| 4 >= 3 // 3 >= 3 ||| 4 >= 4
            cout<<" ";     //             0000                                  000                       00                0
            k--;
        }
        int j = 1; // stars
        while(j <= i){   //  1 <= 1 ||| 1 <= 2 // 2 <= 2  ||| 1 <= 3 // 2 <= 3 // 3 <= 3 ||| 1 <= 4 ... ||| 1 <= 5
            cout<<"* ";  //   0000*          000**                   00***                    0****          *****
            j++;
        }
        cout<<"\n";
        i++;
    }
    // 2nd part
    i = 1;
    while(i < n){
        int j = 1; // spaces
        while(j <= i){ // 1 <= 1 ||| 1 <= 2 // 2 <= 2 ||| 1 <= 3 // 2 <= 3 // 3 <= 3 ||| 1 <= 4 // 1 <= 4 // 3 <= 4 // 4 <= 4 
            cout<<" "; //   0              00                     000                                 0000
            j++;
        }
        int k = n - 1; // stars 4
        while(k >= i){ // 4 >= 1 // 3 >= 1 // 2 >= 1 // 1 >= 1 ||| 4 >= 2 // 3 >= 2 // 2 >= 2 ||| 4 >= 3 // 3 >= 3 ||| 4 >= 4
            cout<<"* ";//                 0****                           00***                        000**            0000*
            k--;
        }
        cout<<"\n";
        i++;
    }
    return 0;
}