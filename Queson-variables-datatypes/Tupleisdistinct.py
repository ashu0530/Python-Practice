#Given a tuple A, find if all elements of tuple are different or not?
# A = (1,2,3,4,5,4) #Output = Not Distinct
# A = (1,2,3,4,5)

A = (1,2,3,4,5,4)
print(set(A))
if len(A) == len(set(A)):  ##Distinct items - no same items is allowed in set so simple comparing lengthbof tuple and length of set
    print("Distinct")
else:
    print("Not distinct")
