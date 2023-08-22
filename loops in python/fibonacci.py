#I/P : n = 4 
#O/P: 1 1 2 3 5
#I/P: n = 5
#O/P: 1 1 2 3 5 8

n = int(input("Please enter n value: "))   #n =5
if n ==0:                                  #print(1,1) a =1,b=1,i=2:c =2 print(2), a=1,b=2
    print(1)                                               #    i=3: c=3,print(3),a=2,b=3
elif n ==1:                                                #    i=4: c=5,print(5),a=3,b=5
    print(1,1)                                             #    i=5: c=8,print(8),a=5,b=8
else:
    print(1,1,end=" ")  #if n is > 1, print two 1, 1 
    a = 1  #define previous two terms as 1 1
    b = 1
    for i in range(2, n+1):
        c = a+b
        print(c, end=" ")
        a=b
        b=c