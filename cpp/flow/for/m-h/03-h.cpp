#include <iostream>
using namespace std;

int main () {
    // program which find all quadriples
    // count how many (a, b, c, d) with following property:
    //    1 <= a, b, c, d <= 200
    //    a + b = c + d

    // 1st try
    int output = 0;
    for (int a = 1; a <= 200; a++) {      // 4 loops
        for (int b = 1; b <= 200; b++) {
            for (int c = 1; c <= 200; c++) {
                for (int d = 1; d <= 200; d++) {
                    if (a + b == c + d)
                        output++;
                }
            }
        }
    }
    cout << output << "\n"; // 5333400

///////////////////////////////////////////////////////////////
	int count = 0;
	for (int a = 1; a <= 200; ++a) {       // 3 loops
		for (int b = 1; b <= 200; ++b) {   //   faster
			for (int c = 1; c <= 200; ++c) {
				int d = a + b - c;    
				if(1 <= d && d <= 200)
					count++;
			}
		}
	}
	cout << count << "\n";   // 5333400

    return 0;
}