# I/P: n = 4
# O/P: *
#      * *
#      * * *
#      * * * *

n = int(input("Please enter the value of n : "))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

#n = 3
# i = 0, j = 0 - *

# i = 1, j = 0 - *
#                *
#        j = 1 - *
#                * *

# i = 2, j = 0 - *
#                * *
#                *
#        j = 1 - *
#                * *
#                * *
#        j = 2 - *
#                * *
#                * * *   