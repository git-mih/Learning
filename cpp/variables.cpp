#include <iostream>
using namespace std;

int main(){
    //Declaring a variable in memory (Garbage value if we dont initialize it)
    int age;

    //Assigning value in memory
    age = 25;
    cout<< age <<"\n";

    //We can also reassign value
    age = 40;
    cout<< age <<"\n";

    cout<<"-----------------\n";
    
    //we can initialize it several ways
    int age0;       //unitialized (garbage value)
    int age1 = 10; //C-style
    int age2 (20); //Constructor initialization
    int age3 {30}; //Modern initialization

    //    642280      10         20         30
    cout<<age0<<" "<<age1<<" "<<age2<<" "<<age3<<"\n";

    cout<<"-----------------\n";

    return 0;
}