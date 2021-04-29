#include <iostream>
using namespace std;

int main() {
    /* 
    first try
    pattern program  test case: 4

    *
    * *
    * * *
    * * * *
     
    */
    int n, i = 0, j = 0;
    cin>>n;

    while(i < n){ // rows  (0 < 4) (1 < 4) (2 < 4) (3 < 4)
        while(j <= i){ // 1st(0 <= 0, 1 <= 1)  2nd(0 <= 2, 1 <= 2, 2 <= 2) 3rd(0 <= 3, 1 <= 3, 2 <= 3, 3 <= 3) ...
            cout<<"* ";//           *                    **                            ***                      ****
            j++;
        }
        j = 0; // we require to reset j. otherwise, we would not be able to check the inner while condition again 
        i++;
        cout<<"\n";
    }

    return 0;
}