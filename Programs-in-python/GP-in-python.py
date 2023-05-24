#Geometric progression nth term in python

#A person gets 5000 as salary on 1st jan 2020, the salary doubles every year. Find the salary that the person will get on 1st jan 2030

#5000,         10000,      20000,       40000,           ......?
#1stjan 2020   1jan2021    1jan2022     1jan2023               1st jan 2030 |

#10000/5000=2 ,  20000/10000=2,  40000/20000=2

#total 11 years = n

#n th term of GP = ar^n-1, Where a = First term, r = common ratio
#5000x2^11-1= 51200000

#a, axr,axrxr,axrxrxr,.........?
#ar^0,ar^1,ar^2,ar^3.........ar^n-1

#I/P = a =2, r= 2, n = 10  
#O/P = 1024

a = int(input("Enter a:"))
r = int(input("Enter r:"))
n = int(input("Enter n:"))
result = a*r**(n-1)
print(result)
