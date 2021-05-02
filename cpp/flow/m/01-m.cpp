#include <iostream>
using namespace std;

int main() {
    // diamond pattern
    // my firts try
    int n;
    cin>>n;

    int row = 1;
    while(row <= n)
    {
        int space = n;
        while(space > row) 
        {   
            cout<<" ";
            space--;
        }
        int star = 1;
        while(star <= row)
        {                  
            cout<<"*";
            star++;
        } 
        int star2 = 1;
        while(star2 < row)
        {
            cout<<"*";
            star2++;
        }
        row++;
        cout<<"\n";
    }

    row = 1;
    while(row <= n)
    {
        int space2 = 1;
        while(space2 < row)
        {
            cout<<" ";
            space2++;
        }
        int star3 = n;
        while(star3 >= row)
        {
            cout<<"*";
            star3--;
        }
        int star4 = n;
        while(star4 > row)
        {
            cout<<"*";
            star4--;
        }
        row++;
        cout<<"\n";
    }

	return 0;
}

