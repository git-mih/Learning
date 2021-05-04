#include <iostream>
using namespace std;

int main () {
    // program which read N, M and SUM. Then find all pairs that has:
    // A + B == SUM             eg sum being 10: 0+10 == 10 // 1+9 == 10 // 2+8 == 10 and so on...
    //    where:                          
    //       1 <= a <= N
    //       1 <= b <= M

    // Faster version
    // 2nd loop was useless as only maximum 1 b will have value that matches sum
    // with simple Math, we can know the possible value of b.
    int N, M, sum;
    cin >> N >> M >> sum; // 10 10 10      we can now perform something like: 1M 1M 1M.

    int steps = 0;

    for (int a = 1; a <= N; a++) { // a=1   //   a=2    //  a=3      ...   a=10

        int b = sum - a; //       (b = 10-1)  (b = 10-2)  (b = 10-3) ... (b = 10-10)
                         //          = 9         = 8         = 7            = 0
        if (1 <= b && b <= M) // (1<=9 && 9<=10) (1<=8 && 8<=10) (1<=7 && 7<=10) ... (1<=0 && 0<=10)
            steps++;          //                                                        F       T
    }

    cout << "steps: " << steps;  // 9

    return 0;
}