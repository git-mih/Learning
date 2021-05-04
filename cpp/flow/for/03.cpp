#include <iostream>
using namespace std;

int main () {
    // program which read N, M and SUM. Then find all pairs that has:
    // A + B == SUM             eg sum being 10: 0+10 == 10 // 1+9 == 10 // 2+8 == 10 and so on...
    //    where:                          
    //       1 <= a <= N
    //       1 <= b <= M

    int N, M;
    cin >> N >> M; // 10 10

    int sum;
    cin >> sum; // 10

    int steps = 0;

    for (int a = 0; 1 <= a <= N; a++) { //     a=0    1 <= a <= 10 // a=1 -> (b=0...b=11) -> a=2 -> b=0 and so on... 
        for (int b = 0; 1 <= b <= M; b++) { // b=11   1 <= b <= 10 whenever b > M, we break out of the loop and a++
            if (a + b == sum) { // (1+1 1+2 1+3 1+4 1+5 1+6 1+7 1+8 1+9 1+10) (2+0 2+1 ...) 
                cout << a << "+" << b << "\n"; // 0+10 // 1+9 // 2+8 ... 
                steps += 1;
            }
            else if (b > M)
                break; // it guarantee a++. otherwise, we would keep doing it forever
        } 
        if (a > N)
            break;
    }
    cout << "steps: " << steps;  // 11

    return 0;
}