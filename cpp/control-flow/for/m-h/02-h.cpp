#include <iostream>
using namespace std;

int main () {
    // program which count how many x, y numbers such
    //   x in range 50-300
    //   x in range 70-400
    //      x < y
    //     (x + y) divisible by 7
    // 1st try
    int output = 0;
    for (int x = 50; x <= 300; x++) {
        for (int y = 70; y <= 400; y++) {
            if (x < y && (x + y) % 7 == 0)
                output++;
        }
    }
    cout << output;

    return 0;
}