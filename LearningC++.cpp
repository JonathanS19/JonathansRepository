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
4)Functions 
#include<iostream>
using namespace std;

void sumofnum(int num1,int num2)
{
    int sum = 0;
    sum = num1+num2;
    cout<<"The sum is "<<sum;

}
int main()
{
    int num1,num2;
    cout<<"Enter the values : ";
    cin>>num1>>num2;
    sumofnum(num1,num2);

}
5)Staircase
a)With star
#include<iostream>
using namespace std;

int main()
{
    int no;
    cout<<"Enter the number of rows : ";
    cin>>no;
    int i,j;
    for(i = 0;i<=no;i++)
    {
        for(j=1;j<=i;j++)
        {
            cout<<"*";
        }
        cout<<endl;
    }
}
b)With Numbers
#include<iostream>
using namespace std;

int main()
{
    int no;
    cout<<"Enter the number of rows : ";
    cin>>no;
    int i,j;
    for(i = 0;i<=no;i++)
    {
        for(j=1;j<=i;j++)
        {
            cout<<j;
        }
        cout<<endl;
    }
}

6)Reverse staircase
#include<iostream> 

using namespace std; 

  

int main() 

{ 

    int no; 

    cout<<"Enter the number of rows : "; 

    cin>>no; 

    int i,j; 

    for(i=no;i>0;i--) 

    { 

        for(j=0;j<i;j++) 

        { 

            cout<<"*"; 

        } 

        cout<<endl; 

    } 

} 

7)Hollow Box
int main()
{
    int no;
    int i,j,spc;
    cout<<"Enter the size : ";
    cin>>no;
    int cnt = 0;
    for(i=1;i<=no;i++)
    {
        cnt = 0;
        for(j=0;j<no;j++)
        {
            if(cnt!=1)
            {
                if(i==1||i==no)
                {
                    cout<<"*";
                }
                else
                {

                    cout<<"*";
                    for(spc=0;spc<(no-2);spc++)
                    {
                        cout<<" ";
                    }
                    cout<<"*";
                    cnt++;
                }
            }
        }
        cout<<endl;
    }

}

/*
Refresh Run 

code - 
#include<iostream>
using namespace std;

int main(){

int size;
int i,j;

cout<<"Enter the size : ";
cin>>size;


for(i=0;i<size;i++)
{
    for(j=0;j<size;j++)
    {
        cout<<"*";
    }
    cout<<endl;
}
}

o/p -
Enter the size : 4
****
****
****
****

code - 
#include<iostream>
using namespace std;

int main()
{
    int rows,cols;
    int n;

    cout<<"Enter the size : ";
    cin>>n;
    n++;
    for(rows=1;rows<n;rows++)
    {
        for(cols=1;cols<=rows;cols++)
        {
            cout<<rows;
        }
        cout<<endl;
    }
}

o/p - 
Enter the size : 5
1
22
333
4444
55555

code - 
#include<iostream>
using namespace std;

int main()
{
    int rows,cols,n,spc;
    cout<<"Enter the size : ";
    cin>>n;

    for(rows=n;rows>=0;rows--)
    {
        for(spc=0;spc<=(n-rows);spc++)
        {
            cout<<" ";
        }
        for(cols=0;cols<=rows;cols++)
        {
            cout<<"* ";
        }
        cout<<endl;
    }
}


o/p - 
Enter the size : 5
 * * * * * *
  * * * * *
   * * * *
    * * *
     * *
      *

code - 

      
*/
