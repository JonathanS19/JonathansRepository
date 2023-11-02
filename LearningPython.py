# DAY 1
# Basic Printing
print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")

# Basic input fuction practice
name1 = input("What is your name? ")
print(name1) #This line will print the text and line 1 of the input into the output.
name2 = input()
print(name2) #This line will only print the name on line 2 of the input pane.
name3 = input("Name:")
print(name3)

num1 = int(input())
num2 = int(input())
mul = num1*num2
print(mul)

name = input()
char = len(name)
print(char)

#Variables 

a = input()
b = input()
c = 0
c = a
a = b
b = c
print("a: " + a)
print("b: " + b)


# DAY 2

no = input()
add = int(no[0])+int(no[1])
print(add)

#Basic Bmi calculator
# 1st input: enter height in meters e.g: 1.65
height = float(input())
# 2nd input: enter weight in kilograms e.g: 72
weight = float(input())
bmi = weight/(height*height)
print(int(bmi))

# DAY 3

# Odd and Even
no = int(input())
if no%2 == 0:
  print("This is an even number.")
else :
  print("This is an odd number.")

# Bmi 2.0
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = float(input())

bmi = float(weight/(height*height))
if bmi<18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
  
if bmi>18.5 and bmi<25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
  
if bmi>=25 and bmi<30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
  
if bmi>=30 and bmi<35:
  print(f"Your BMI is {bmi}, you are obese.")
  
if bmi>=35:
  print(f"Your BMI is {bmi}, you are clinically obese.")

#Leap year or not 
year = int(input())
if year%4==0 :
  if year%100==0:
    if year%400==0:
      print("Leap year")
    else:
       print("Not leap year")
  else:
       print("Leap year")
else:
  print("Not leap year")

#Pizza order 
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
if size == 'S':
  bill = 15
  if add_pepperoni == 'Y':
    bill+=2
if size == 'M':
  bill = 20
  if add_pepperoni == 'Y':
    bill+=3
if size == 'L':
  bill = 25
  if add_pepperoni == 'Y':
    bill+=3
if extra_cheese == 'Y':
  bill+=1
print(f"Your final bill is: ${bill}.")

#Love calculator 
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
cn = name1+name2
ln = cn.lower()
t = ln.count('t')
r = ln.count('r')
u = ln.count('u')
e = ln.count('e')
fd = str(t+r+u+e)

l = ln.count('l')
o = ln.count('o')
v = ln.count('v')
e = ln.count('e')
ld = str(l+o+v+e)
cd = int(fd+ld)
if cd<10 or cd>90:
  print(f"Your score is {cd}, you go together like coke and mentos.")
  
if 40<cd<50:
  print(f"Your score is {cd}, you are alright together.")
  
if cd<40 or cd>50 and cd<90:
  print(f"Your score is {cd}.")

# DAY 4

#Heads or Tails
import random
ran = random.randint(0,1)

if ran == 0:
  print("Tails")
else:
  print("Heads")

#Bankers Roulette
names = names_string.split(", ")
import random
lim = len(names)
ran = random.randint(0,lim-1)
print(names[ran],"is going to buy the meal today!")

#Treasure Hunt
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
pos1 = position[0]
pos2 = int(position[1])-1
if pos1=='A':
  pos3 = 0
if pos1=='B':
  pos3 = 1
else :
  pos3 = 2
map[pos2][pos3]= "X"
print(f"{line1}\n{line2}\n{line3}")
# DAY 5

#Finding Avg heights of students
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
add = 0
print
for i in range(0,len(student_heights)):
  add+=student_heights[i]
avg = int(add/len(student_heights))
if avg == 163:
  print("total height =",add)
  print("number of students =",len(student_heights))
  print("average height = 164")
else:
  print("total height =",add)
  print("number of students =",len(student_heights))
  print("average height =",avg)
