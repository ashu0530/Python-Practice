#Given a tuple A with distinct elements and an integer X, find the index position of X. Assume to have X in tuple always.

#A = (1,2,3,4,5), X = 3
#output = 2

A = (1,2,3,4,5)
X = 3
for i in range(len(A)):
    if A[i]==X:
        print(i)

print(A.index(X)) #second method