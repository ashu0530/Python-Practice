#Finding all divisor of a number
#I/P: 12
#O/P: 1,2,3,4,6,12

n =int(input("Please enter a value: "))
if n <=0:
    print("Enter positive value")
else:
    for i in range(1,n+1):
        if n%i == 0:
            print(i)


n =int(input("Please enter a value: "))
x=1
while x<=n:
    if n%x==0:
        print(x)
    x = x+1

#optimised solution for all divisor
n =int(input("Please enter a value: "))
x=1
while x*x<=n:
    if n%x==0:
        print(x)
        print(n/x)
    x = x+1
if x*x ==n:
    print(x)
