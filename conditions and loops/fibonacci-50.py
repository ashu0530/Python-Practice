'''
Here's an iterative algorithm for printing the Fibonacci sequence:
Create 2 variables and initialize them with 0 and 1 (first = 0, second = 1)
Create another variable to keep track of the length of the Fibonacci sequence to be printed (length)
Loop (length is less than series length)
Print first + second
Update first and second variable (first will point to the second, and the second will point to first + second)
Decrement the length variable and repeat from step 3
Once the loop terminates, terminate the program
'''
#using for loop
num1=0
num2=1

for i in range(50):
    print(num1)
    num1,num2=num2,num1+num2

#using variable
first=0
second=1

for j in range(50): 
    print(first) #one first iterate=0, 2nd iterate = 1, 3rd iterate=
    temp=first #temp =0, temp=1, temp=1
    first=second #first=1, first=1, first=3
    second = temp+second #second=1, second=3, second=4
    