#Find the smallest divisor of a number such that the divisor is greater than 1
#I/P : n=6  , n=49, N=13
#O/P: 2, o/p=7  ,O/P = 13

n = int(input("Please enter value"))
for i in range(2,n+1):
    if n%i ==0 :
        print(i)
        break


n = int(input("Please enter value"))
x = 2
while x<=n:
    if n%x == 0:
        print(x)
        break  #out of the loop 
    x = x+1 #increment of x

i = 1
while i <= 5:   #1sttrue #2nd true #3rd true
    if i == 3:   #true is 3==3
        break   #break the loop   
    print(i)  #1 #2         |
    i = i+1   #2 #3         |
print(i)        #           jump to here print i = 3    

#op = 1,2,3


