#A number is a prime number which is divisible by 1 and number only
#2,3,5,7,11,13,17

n = int(input("Please enter the value: "))

if (n<=1):
    print("No")
else:
    for i in range(2,n): #2 to 90 in case of 91 #7divide 91
        if (n%i==0):
            print("No")
            break
    else:
        print("Yes prime")
