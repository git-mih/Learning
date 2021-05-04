#include <iostream>
using namespace std;

int main () {
    // program which read N, M, W. then find all triples that has
    // A + B <= C             
    //    where:                          
    //       1 <= A <= N
    //       A <= B <= M 
    //       1 <= C <= W
    int N, M, W;
    cin >> N >> M >> W; // 100 200 20

    int steps = 0;

    for (int a = 1; a <= N; a++) {     
        for (int b = a; b <= M; b++) { 
            for (int c = 1; c <= W; c++) { 
                if (a + b <= c)  
                    steps++;
            }
        } 
    }

    cout << "steps: " << steps;  // 715

    return 0;
}