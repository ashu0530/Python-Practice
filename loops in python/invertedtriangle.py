#I/P: n = 4
#O/P  * * * *
#     * * *
#     * *
#     *

n = int(input("Please enter the value: "))
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()