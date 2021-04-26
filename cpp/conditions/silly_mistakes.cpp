#include <iostream>
using namespace std;

int main()
{
    //silly mistakes

    //1
    int age = 11;
    if(age = 22) // reassigning value
        cout<<age<<"\n"; // 22

    //2
    if(age) // if(22) = true
        cout<<age<<"\n"; // 22

    //3
    int a {25};
    if (a < 10); // sadly we closed this if statement here 
		cout << 1; // then 1 will be printed

	if (a < 20)  // now control will check if 25 < 20 (false) then the control will jump to the else statement
		cout << 2;
	else
		cout << 3; // 3 will be printed

    //4
    int b {5};
    if (b < 10)
		cout << 1; // we also closed the if statement here.
		cout << 2; // 12 will be printed (1 and 2)

    //5    
	if (true){ 
        {   // no problem to do it at all
			int x  = 0;
          //++x;   would work
		}
      //++x;       x cant be used in this scope. we can use it inside {} above, not outside it.
	}
	cout<<"bye\n"; // bye

    return 0;
}