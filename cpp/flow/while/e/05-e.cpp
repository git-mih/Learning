#include <iostream>
using namespace std;

int main(){

    // first try
    // program which will read integer n. then get n numbers and print 2 values:
    // 1. the average of the numbers in Odd positions (1st, 3rd, 5th, ...) 
    // 2. the average of the numbers in Even positions (2nd, 4th, 6th, ...)
    // test case: 3  (10 20 30)   ->  output must be: (20 20) odd(10+30)/2 = 20, even(20)/1 = 20
    int n;
    cin>>n; // 3

    int num; // responsible to greb the inputs
    int sum_odd = 0, sum_even = 0; // (0+10+30) (0+20)

    int i = 1; // 1 cause i rather start with the odd value (1%2 != 0)
    int odd_cnt = 0, even_cnt = 0; // we gonna use it to count how many odds/even numbers we will find, so we can take the average.

    while(i <= n){ // (1 <= 3) (2 <= 3) (3 <= 3)
        if(i % 2 != 0){ // (1) (0) (1)
            cin>>num; // 10 30
            sum_odd += num; //sum_odd = (0+10) (10+30)
            odd_cnt++; // 1, 2 ,3
            i++;
        }else{
            cin>>num; // 20
            sum_even += num; //sum_even = (0+20)
            even_cnt++; // 1, 2
            i++;
        }
    }

    int odd_av = sum_odd/odd_cnt;    // sum of odd values divided by the number of odd values we find
    int even_av = sum_even/even_cnt; // same to even

    cout<<odd_av<<"\n";
    cout<<even_av<<"\n";

    return 0;
}