0)Basics 
a)Voter
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int age;
    printf("Enter your age : ");
    scanf("%d",&age);

    if(age<18)
    {
        printf("Too Young to vote !");
    }
    else
        printf("You can vote!!");
}

1)Print the month 

#include <stdio.h>
#include <stdlib.h>
int main()
{
    int month;
    printf("Enter the number of month you want: ");
    scanf("%d",&month);
    if (month == 1){
        printf("January\n ");
    }
    else if(month == 2) {
        printf("February\n");
    }
    else if(month == 3) {
        printf("March\n");
    }
    else if(month == 4) {
        printf("April\n");
    }
    else if(month == 5) {
        printf("May\n");
    }
    else if(month == 6) {
        printf("June\n");
    }
    else if(month == 7) {
        printf("July\n");
    }
    else if(month == 8) {
        printf("August\n");
    }
    else if(month == 9) {
        printf("September\n");
    }
    else if(month == 10) {
        printf("October\n");
    }
    else if(month == 11) {
        printf("November\n");
    }
    else if(month == 12) {
        printf("December\n");
    }
    else {
        printf("Where are you from ??\n");
    }
    return EXIT_SUCCESS;
}

2)Average of 3 numbers :

#include<stdio.h>
#include<stdlib.h>
int main()
{
    int num1,num2,num3;
    printf("Enter any 3 numbers :");
    scanf("%d%d%d",&num1 ,&num2 ,&num3);
    int sum = num1+num2+num3;
    float avg = sum/3;
    printf("The average of %d,%d and %d is %.2f",num1,num2,num3,avg);
    
}
3)Greatest of 3 numbers :

method 1 )

#include<stdio.h>
#include<stdlib.h>
int main()
{
    int num1,num2,num3;
    printf("Enter 3 numbers: ");
    scanf("%d%d%d",&num1,&num2,&num3);
    int max = num1;
    if (max<num2)
    {
        max = num2;
    }
    if (max<num3)
    {
        max = num3;
    }
    printf("The maximum is %d",max);
}

method 2)

#include<stdio.h>
#include<stdlib.h>
int main()
{
    int num1,num2,num3;
    printf("Enter 3 numbers: ");
    scanf("%d%d%d",&num1,&num2,&num3);
    if(num1>num2 && num1>num3)
    {
        printf("The greatest is %d",num1);
    }
    else if (num2>num3){
        printf("The greatest is %d",num2);
    }
    else 
    {
        printf("The greatest is %d",num3);
    }
}

4)Reversing a array:

Method 1)
//A rather easy method 
#include<stdio.h>
#include<stdlib.h>
#include"Functions.c"
int main()
{
    int temp,i,j;
    int arr[]={12,18,97,56,74,57};
    int size = sizeof(arr)/sizeof(arr[0]);

    printf("Before reversal : ");
    printarr(arr,size);
    for(i=0,j=size-1;i<j;i++,j--)
    {
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    printf("After reversal : ");
    printarr(arr,size);
}



Method 2)

#include<stdio.h>
#include<stdlib.h>
#include"Functions.c"
int main()
{
    int i,j,temp;
    int arr[] = {10,23,54,65,44,86,36,77};
    int size = sizeof(arr)/sizeof(arr[0]);

    printf("Array before reversing :");
    printarr(arr,size);
    //assigning values to i and j

    for(i=0,j=size-1;i<j;i++,j--)
    {
           temp = arr[i];
           arr[i] = arr[j];
           arr[j] = temp;

    }
    printf("Array after reversing : ");
    printarr(arr,size);
}

//Same think but i have included a built in function of my own :)

//This is the function :
void enterval(int arr[],int n)
{
    printf("Enter the values of the array :\n");
    for(int i=0;i<n;i++)
    {
        printf("Element %d: ",i);
        scanf("%d",&arr[i]);
        printf("\n");
    }
}
//The normal code follows below :
#include<stdio.h>
#include<stdlib.h>
#include"Functions.c"
int main()
{
    int i,j,temp;
    int arr[4];
    int size = sizeof(arr)/sizeof(arr[0]);
    enterval(arr,size);

    printf("\nArray before reversing :");
    printarr(arr,size);
    //assigning values to i and j

    for(i=0,j=size-1;i<j;i++,j--)
    {
           temp = arr[i];
           arr[i] = arr[j];
           arr[j] = temp;

    }
    printf("\nArray after reversing : ");
    printarr(arr,size);
}

5)Strings

i)Working with strings :
#include<stdio.h>
#include<stdlib.h>
#include"Functions.c"
int main()
{
    char name[30];
    printf("Enter Your name :");
    //scanf("%s",&name); This causes the input to break at the sight of a space
    fgets(name,sizeof(name),stdin);
    printf("Normal Name: %s",name);
    name[0] = "X";
    printf("Name with X : %s",name);
}

6)Factorial

#include<stdio.h> 

#include<stdlib.h> 

int main() 

{ 

    int no; 

    int fact = 1; 

    printf("Enter the Number whose factorial you want : "); 

    scanf("%d",&no); 

  

    if (no == 1 ) 

    { 

        printf("1 = 1"); 

    } 

    else 

    { 

            for(int iter = 1;iter<=no;iter++) 

    { 

        if(iter!=no) 

        { 

            printf("%d * ",iter); 

        } 

        else 

        { 

            printf("%d",iter); 

        } 

        fact = fact*iter; 

    } 

    printf(" = %d",fact); 
}
7)Prime nos from 1 to 100 

 

#include<stdio.h> 

#include<stdlib.h> 

int main() 

{ 

    int no,i,j; 

    int cnt; 

    printf("Prime numbers from 1 to 100 \n"); 

    for(i=2;i<=100;i++) 

    { 

        cnt=0; 

        for (j=1;j<=100;j++) 

        { 

            if(i%j==0) 

            { 

                cnt++; 

            } 

        } 

        if(cnt==2) 

        { 

            printf("%d\n",i); 

        } 

    } 

} 
8)Patterns

a)Diamond
#include<stdio.h>
#include<stdlib.h>
int main()
{
    //Initialization
    int row,col;
    int size,spc;
    printf("Enter the number : ");
    scanf("%d",&size);

    //Upper Pyramid
    for(col = 0;col<size;col++)
    {
        for(spc = col;spc<=size;spc++)
        {
            printf(" ");
        }
        for(row = 0;row<col;row++)
        {
            printf(" *");
        }
        printf("\n");
    }


    //Lower Pyramid
    for(col = size-1;col>=0;col--)
    {
        for(spc = 0;spc<size-col;spc++)
        {
            printf(" ");
        }
        for(row = 0;row<=col;row++)
        {
            printf(" *");
        }
        printf("\n");
    }

}

b)Rhombus 
#include<stdio.h>
#include<stdlib.h>
int main()
{
    //Initialization
    int cols,rows;
    int spc,no;
    printf("Enter the size : ");
    scanf("%d",&no);

    //Creating the Rhombus
    for(cols = 0;cols<no;cols++)
    {
        for(spc = 0 ;spc < (no-1)-cols; spc++)
        {
            printf(" ");
        }
        for(rows = 0;rows<no;rows++)
        {
            printf("*");
        }
        printf("\n");
    }
}

c)Butterfly Pattern
#include<stdio.h>
#include<stdlib.h>
int main()
{

    //Initialization
    int cols,rows;
    int spc,no;
    printf("Enter the size : ");
    scanf("%d",&no);
    int var = no*2;
    int var1 = 2;
/*
    Top Half

    //First Wing
    //Upper Triangle
    for(cols = 0;cols<=no;cols++)
    {
        for(rows = 0;rows<cols;rows++)
        {
            printf("*");
        }
        printf("\n");
    }
    //Second Wing
    //Upper Triangle
    for(cols = 0;cols<=no;cols++)
    {
        for(spc = 0;spc<(no-cols);spc++)
        {
            printf(" ");
        }
        for(rows = 0;rows<cols;rows++)
        {
            printf("*");
        }
        printf("\n");
    }
*/
    //Fused Top half
    for(cols = 0;cols<=no;cols++)
    {
        for(rows = 0;rows<cols;rows++)
        {
            printf("*");
        }

        for(spc = 0;spc<=var+1;spc++)
        {
            printf(" ");
        }
        for(rows = 0;rows<cols;rows++)
        {
            printf("*");
        }
        var = var - 2;
        printf("\n");

    }
/*
     Lower Half
        for(cols = no;cols>0;cols--)
    {
        for(rows = no;rows>(no-cols);rows--)
        {
            printf("*");
        }
        printf("\n");
    }
        for(cols = no;cols>0;cols--)
    {
        for(spc = 0;spc<(no-cols);spc++)
        {
            printf(" ");
        }
        for(rows = 0;rows<cols;rows++)
        {
            printf("*");
        }
        printf("\n");
    }
*/

    //Attempt at fusing Lower Half
    for(cols = no;cols>0;cols--)
    {
        for(rows = no;rows>(no-cols);rows--)
        {
            printf("*");
        }
        for(spc = 0;spc<var1;spc++)
        {
            printf(" ");
        }
        for(rows = 0;rows<cols;rows++)
        {
            printf("*");
        }
        var1 = var1+2;
        printf("\n");
    }
}
9)While loops 

//a)Powers of a number

#include<stdio.h>
#include<stdlib.h>
int main()
{
//Initialization
int no,mul;
int power,iter = 1;
printf("Enter the number : ");
scanf("%d",&no);
mul = no;
printf("Enter the power : ");
scanf("%d",&power);

//Multiplying
while(iter!=power)
{
    mul = mul * no;
    iter++;
}
printf("%d^%d = %d",no,power,mul);
}

//b)Multiplication tables with while
#include<stdio.h>
#include<stdlib.h>
int main()
{
//Initialization
int no,result;
printf("Enter a number : ");
scanf("%d",&no);
int iter = 1;
while(iter!=11)
{
    result = no*iter;
    printf("%d x %d = %d\n",no,iter,result);
    result = 0;
    iter++;
}
}

c)//Factorial using while
#include<stdio.h>
#include<stdlib.h>
int main()
{
//Initialization
int no,fact=1;
printf("Enter a number : ");
scanf("%d",&no);
int iter = 1;
while(iter!=no+1)
{
    fact = fact*iter;
    printf("%d",iter);
    while(iter!=no)
    {
        printf("*");
        break;
    }
    iter++;
}
printf(" = %d",fact);
}

//d)Sum of digits 
#include<stdio.h>
#include<stdlib.h>
int main()
{
    //Initialization
    printf("Sum of digits\n");
    int iter,no;
    printf("Enter a number : ");
    scanf("%d",&no);
    int sep,sum;
    int copy = no;
    //Seperating digits
    while(no!=0)
    {
        sep = no%10;
        no = no/10;
        sum = sum + sep;
    }
    printf("The sum of the digits %d is %d",copy,sum);

}

//e)Reversing numbers 
#include<stdio.h>
#include<stdlib.h>
int main()
{
    //Initialization
    int rev = 0;
    int no,seperate;
    printf("Enter the number : ");
    scanf("%d",&no);

    //Reversing process
    while(no!=0)
    {
       seperate = no%10;
       no = no/10;
       rev = rev*10+seperate;
    }
    printf("The reverse is %d",rev);
}

9)Strings
a)String Copy 

#include<stdio.h>
#include<stdlib.h>
int main()
{
    //Initialization
    int size;
    printf("Enter the size of the array : ");
    scanf("%d",&size);
    char arr[size];
    char copy[size];
    int i,j;

    //Taking the string
    printf("Enter the String  : ");
    for(i=0;i<size;i++)
    {
        scanf(" %c",&arr[i]);
    }
    printf("\nThe original string is : ");
    for(j = 0;j<size;j++)
    {
        printf("%c",arr[j]);
    }

    //Making a copy
    for(i=0;i<size;i++)
    {
        copy[i] = arr[i];
    }
    printf("\nCopied String : ");
    for(j = 0;j<size;j++)

    b)String Anagram
    #include<stdio.h>
#include<stdlib.h>
int main()
{
    //Initialization
    int size;
    int i,j,count = 0;
    printf("Enter the size of the word : ");
    scanf("%d",&size);
    char word1[size],word2[size];

    //Taking the 2 words
    printf("\nEnter the 1st word : ");
    for(i=0 ;i<size; i++)
    {
        scanf(" %c",&word1[i]);
    }

    printf("\nEnter the 2nd word : ");
    for(i=0 ;i<size; i++)
    {
        scanf(" %c",&word2[i]);
    }

    //Checking for anagrams
    for(i=0;i<size;i++)
    {
        for(j=0;j<size;j++)
        {
            printf("\nI = %c",word1[i]);
            printf("\nJ = %c",word2[j]);
            printf("\nCnt = %d",count);

            if(word1[i] == word2[j])
            {
                count++;
                break;
            }
        }
    }
    if(count == size)
    {
        printf("\nIt is a anagram");
    }
    else
    {
        printf("\nIt is not a Anagram");
    }
}
    {
        printf("%c",copy[j]);
    }
}
c)String Reversal :
#include<stdio.h>
#include<stdlib.h>
int main()
{
    //Initialization
    int size,count;
    printf("Enter the String Size: ");
    scanf("%d",&size);
    char arr[size];
    int temp,i,j;

    //Taking in a string
    printf("Enter the string : \n");
    for( i = 0 ;i<size;i++)
    {
        scanf(" %c",&arr[i]);
    }
    printf("Original String: ");
    for(i=0;i<size;i++)
    {
        printf("%c",arr[i]);
    }
    printf("\n");

    //Reversing String

   for(i=0,j=size-1;i<j;i++,j--)
   {
       temp = arr[i];
       arr[i] = arr[j];
       arr[j] = temp;
   }

    printf("Reversed string is :");
    for(i=0;i<size;i++)
    {
        printf("%c",arr[i]);
    }
}

10)// Area of circles using macro :

Area of circle using macro :

#include<stdio.h> 
#include<stdlib.h>
#define Pi 3.14
#define square(x) (x*x)
// area of circle = pi*r^2
int main()
{
int radius;
float area;
printf("Enter the radius : ");
scanf("%d",&radius);
area = Pi*square(radius);
printf("Area is %.2f",area);
}
