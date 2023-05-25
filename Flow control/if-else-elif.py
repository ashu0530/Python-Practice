#if condition:
    #Statement to be executed
    #if statement is true
#else:
    #statement to be executed
    #if condition is NOT true

#even or odd
x = int(input("Enter the num: "))
if (x%2)==0:
    print("Even")
else:
    print("odd")

#Positive-negative or zero number
y = int(input("Enter the number: "))
if y<0:
    print("negative")
elif y>0:
    print("positive")
else:
    print("zero")

#Decide if an input number is +even +odd, negative even, negative odd, zero

n = int(input("Enter the num: "))
if n > 0:
    print("positive", end=" ")
    if n%2==0:
        print("even")
    else:
        print("odd")
elif n < 0:
    print("Negative", end=" ")
    if n%2==0:
        print("even")
    else:
        print("odd")
else:
    print("zero")


#take 2 num a and b a>b or b>a or a and b are same

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

if a>b:
    print("a is greater")
elif a<b:
    print("b is greater")
else:
    print("a and b are same")