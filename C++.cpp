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

3)Working with arrays 
    #include<iostream>
using namespace std;

int main()
{
    int size;
    cout<<"Enter the size of the array : ";
    cin>>size;
    int arr[size];
    int i = 0;
    int j = 0;
    int sum = 0;
    cout<<"Enter the array values : ";
    while(i<size)
    {
        cin>>arr[i];
        i++;
    }

    while(j<size)
    {
        sum = sum + arr[j];
        j++;
    }
    cout<<"The sum of the arrays is : "<<sum;
}

