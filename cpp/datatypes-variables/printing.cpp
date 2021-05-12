#include <iostream>
using namespace std;

int main(){
    //spell cout<<"text" together.
    cout<<"It is good practice\n";

    cout<<endl; //new line

    //We can have several print commands
    cout<<"Hi, i am "<<"fabio"<<endl<<"im 26\n";
    cout<<"and love mathmatics!!";
    cout<<endl;

    cout<<endl;

    //all of the above code in the same line with 6 print statements
    cout<<"Hi, im"<<"fabio"<<endl<<"im 26\n"<<"and love mathmatics!!"<<endl;
    
    cout<<endl;

    //more readable format
    cout<<"Hi, im fabio"
        <<endl<<"im 26"
        <<endl<<"and love mathmatics!!"
        <<endl;

    cout<<endl;

    //by using only one print statement
    cout<<"Hi, im fabio\nim 26\nand love mathmatics!!\n";

    cout<<"-----------------------\n";

    //we can also print numbers and perform arithmetic
    cout<<10<<"\n"; //10
    cout<<"10+10+5 = "<<10+10+5<<"\n";//25
    cout<<"12/2 = "<<12/2<<"\n";//6
    cout<<"7/2 = "<<7/2<<"\n";     //3  - div w/ 2 integer will provide a integer
    cout<<"7.0/2 = "<<7.0/2<<"\n"; //3.5  - if we provide at least 1 float/double value, it will provide a double
    cout<<"10^9 = "<<10*10*10*10*10*10*10*10*10<<"\n"; //1000000000
    cout<<"10^10 = "<<10*10*10*10*10*10*10*10*10*10<<"\n"; //1410065408  - it will overflow

    return 0;
}