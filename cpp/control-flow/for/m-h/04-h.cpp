#include <iostream>
using namespace std;

int main () {
    // program which read an integer n (2 < n < 500) and print YES if it is prime, otherwise print NO.
    // 1st try
    int n;
    cin >> n;

    string is_prime;               //  case: 4     case: 5
    for (int i = 1; i <= n; i++) { //    (1 <= 4)    (1 <= 5)
        for (int j = 2; j < n; j++) { // (2 < 4)     (2 < 5 // 3 < 5 // 4 < 5)
            if (n % j == 0) 
                is_prime = "NO"; // 4 % 2 == 0? yes, it is prime.
        }                      // 5 % 2 == 0? no // 5 % 3 == 0? no // 5 % 4 == 0? no.
        if (n % i != 0)
            is_prime = "YES";
    }

    cout << is_prime;
    return 0;
}