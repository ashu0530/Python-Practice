#I/p n = 5
#O/P       *
#         ***
n = int(input("Please enter the value"))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for k in range(2*i+1):
        print("*", end=" ")
    print()