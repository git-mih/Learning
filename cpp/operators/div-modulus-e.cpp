#include <iostream>
using namespace std;

int main(){
    // playing with some averages
    int a=1, b=2, c=3, d=4, e=5;
    cout<<(a+b+c+d+e)/5<<"\n";
    cout<<(double)(a+b+c)/(double)(d+e)<<"\n"; //0.666667
    cout<<(double)((a+b+c)/3.0)/(double)((d+e)/2.0)<<"\n";//0.444444

    cout<<"-------------\n";

    // program that read 2 numbers x,y and divides then (a/b), but print only the fraction part.
    double x,y;
    cin>>x>>y; //lets try 201 25
    double result = x/y; 
    cout<< result <<"\n"; // 8.04
    cout<< result - (int)result<<"\n"; //8.04 - 8 = 0.04

    cout<<"-------------\n";

    // program that reads 2 numbers and print the reminder without using % operator.
    int n, m;
    cin >> n >> m; // lets try 13/5
    // 13/5 = 2  [2 complete units, each is 5]
    // 2*5 = 10  [total complete units]
    // reminder is 13-10 = 3. This number generates the fractional part
    int result3 = n - (n / m) * m;

    cout<<"without %: "<<result3<<"\n";
    cout<<"by using %: " <<n % m<< "\n";

    return 0;
}
