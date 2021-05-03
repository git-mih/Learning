#include <iostream>
using namespace std;

int main(){
    // program which read a integer n, then reads n strings and print only the strings of 2 letters
    // these 2 letters must be letter 'n' and letter 'o'
    //    regardless of upper/lower case
    //    regardless of those 2 letters order
    // eg: 'no', 'ON', 'No' would be printed
    // eg: 'NooOo', 'yes', 'OOON' will be ignored and not printed

    // 1st try

    int n;
    cin >> n; // test case: 9  Yss NO nooOO oN Monst no nN oOOoo oO   (gonna take 9 strings)
              // output: NO oN no  

    while (n) { // 9 8 7 ... 0
        string str; 
        cin>>str;
        if (str == "On" || str == "on" || str == "oN" || str == "ON" || str == "No" || str == "no" || str == "nO" || str == "NO") {
            cout<<str<<" ";
        }
        n--;
    }

    return 0;
}