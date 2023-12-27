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
8)Diamond 

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

//Factorial using while
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
