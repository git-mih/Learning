#include <iostream>
using namespace std;

int main() {
    // power funtion program by using while only
    int b, pow;  // base and exponent
    cin>>b>>pow; // test case: 2 3  -> 2^3 = 8

    int result = 1;

    while(pow > 0){ // (3 > 0) (2 > 0) (1 > 0) (0 > 0)
        result *= b; // result = 1 then (1*2 = 2) -> (2*2 = 4) -> (4*2 = 8)
        pow--; // pow started being 3, it will decrease till condition fails
    }

    cout<<result<<"\n"; // 8

    return 0;
}