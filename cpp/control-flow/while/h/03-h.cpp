#include <iostream>
using namespace std;

int main(){
    // program which read a integer n and m, then print n*m lines for their multiplication table.
    // input: 2 4
    /* eg:
           1*1   2*1
           1*2   2*2
           1*3   2*3
           1*4   2*4
    */
    // 1st try

    int n, m;
    cin >> n >> m; // test case: 2 4

    int i = 1;
    while (i <= n) { // (1<=2)  (2<=2)
        int j = 1;
        while (j <= m) { // (1<=4) (2<=4) (3<=4) (4<=4)
            cout << i << "x" << j << " = " << i * j << "\n"; // (1*1 1*2 1*3 1*4) (2*1 2*2 2*3 2*4) ...
            j++; // (j = 1 2 3 4)
        }
        i++; // i=1 i=2
        cout << endl;
    }
    return 0;
}