#include <iostream>
#include <climits>

using namespace std;

int main(){

    //Fundamental datatypes
    int age = 10;
    float pi = 3.14;    //32 bit precision for floating point number. 1 bit for the sign, 8 bits for the exponent, and 23* for the value
    double frac = 2.5;  //64 bit precision for floating point number. 1 bit for the sign, 11 bits for the exponent, and 52* bits for the value
    char letter = 'A';
    string phrase = "hello"; //Collection of characters data type
    bool is_married = true; //true or false = 1 or 0

    //printing them
    cout<<age<<"\n"; //10
    cout<<pi<<"\n";    //3.14  - float has 7 decimal digits of precision
    cout<<frac<<"\n";  //2.5   - double has 15 decimal digits of precision
    cout<<letter<<"\n";  //A
    cout<<phrase<<"\n";  //hello
    cout<<is_married<<"\n"; // 1

    cout<<"----------\n";

    int a = 10;
    int b = 5.0;
    double result = (a + b)/2.0; //7.5  - we require to provide at least one decimal number. Otherwise, it will return a integer
    cout<<result<<"\n";

    cout<<"----------\n";

    /*
    Datatypes max/min values
    char       -128 to 127 (255 unsigned)
    short      -32768 to 32767 (65535 unsigned)
    int        -2147483648 to 2147483647 (4294967295 unsigned) 
    long long  -9223372036854775808 to 9223372036854775807 (18446744073709551615 unsigned)
    */

    // Using constant values of limits.h/climits library
    cout<<"int overflow: \n";
    cout<<"2147483647 + 1 = " <<INT_MAX + 1<<"\n"; //-2147483648  - We will get a integer overflow warning msg. 

    cout<<"----------------\n";

    return 0;
}