#I/P: a = 4 , b = 6
#O/P: 12

#MAX of a and b is 6
#Multiple of a and b is 24
#so lcm lies between 6 and 24



a = int(input("Please enter first value: "))
b = int(input("Please enter second value: "))

if a>b:
    res = a
else:
    res = b   #finding the max of a and b
while (res <= a*b):     #Multiple of a and b is 24
    if ( res % a ==0 ) and (res % b ==0): #checking 
        break;
    res = res+1
print("LCM is", res)


import math
a = int(input("Please enter first value: "))
b = int(input("Please enter second value: "))

gcd = math.gcd(a,b)
lcm = (a*b)/gcd        #a*b = lcm * gcd , lcm = a*b/gcd 
print("Lcm is", lcm )  