#include <iostream>
using namespace std;

int main() {
    /*
    first try
    pattern program

    * * * *
    * * *
    * *
    *
    
    */
    int n;
    cin>>n; // test case: 3

    int j = n; // j starts being 3 and we require to decrease it
    while(n > 0){ // (3 > 0)  (2 > 0) (1 > 0)
        j = n; // decreasing j. j will become 3, now it can print one less star.
        while(j > 0){ // 1st(3 > 0, 2 > 0, 1 > 0)  2nd(2 > 0, 1 > 0)  3rd(1 > 0)
            cout<<"* "; //         ***                **           * 
            j--;
        }
        cout<<"\n";
        n--;
    }
    return 0;
}