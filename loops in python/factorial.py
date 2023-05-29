#Count of arrangement 1x2x3x4x...n
#N! = (n*(n-1)!)
#1!=1
#0! = 1

n = int(input("Enter n"))
res = 1
for i in range(2, n+1):
    res = res*i
print("Factorial is", res)


import math
n = int(input("Enter n"))
res = math.factorial(n)
print("Factorial is", res)


