#include <iostream>

using namespace std;

int main(){
    //To get data from user we require to use cin>>  (console input) 
    int age;
    cout<<"Enter your age: "; // user provide value 20
    cin>>age; // user provide value 2. this value will be assigned to the variable called age

    cout<<"age = "<<age<<"\n"; // age = 20

    cout<<"---------------\n";

    int a, b;
    cout<<"Enter 2 numbers: ";
    cin>>a >>b; // 5 2
    cout<<"The sum of a + b = "<< a + b<<"\n"; // 7

    cout<<"---------------\n";

    //Constants
    const int AGE = 10; //we cant change this value anymore. If we try to: (age = 20;), compiler will stop the program
    const double PI {3.14159}; // better use CAPITAL letters for const variables. Better initialize by using {}
    const char LETTER {'A'};
    const string PHRASE = "Hello";
    //const int x;   unitialized const provides compilation error
    //we also have predefined constants values like: INT_MAX from limits.h/climits library

    cout<<"printing constants \n";
    cout<<AGE    <<endl;
    cout<<PI     <<endl;
    cout<<LETTER <<endl;
    cout<<PHRASE <<endl;
    return 0;
}