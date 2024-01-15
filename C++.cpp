1)Voter 
#include<iostream>
using namespace std;
int main()
{
    int age;
    cout<<"Enter your age : ";
    cin>>age;

    if(age<18)
        cout<<"Go to kindergarden !!";
    else
        cout<<"You can vote !";
}

2)Multi Table
#include<iostream>
using namespace std;

int main()
{
    int no;
    int i = 1;
    cout<<"Enter the number : ";
    cin>>no;

    while(i<=10)
    {
        cout<<no<<"*"<<i<<" = "<<no*i<<endl;
        i++;

    }
}

