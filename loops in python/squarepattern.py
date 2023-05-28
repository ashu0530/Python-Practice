#I/P : n = 3
#O/P : * * *
#      * * *
#      * * *

n = int(input("Please enter number: "))  #Input  
for i in range(n):  #run a loop is 0 to n-1 means n times
                               #Till here it will print vertically * #if you print here
    for j in range(n):   #inner loop iteration
        print("*", end=" ")  #nsquare times we run and end use for space
    print()  #one row is printed we print in new line


# i = 0, j = 0: *
#        j = 1: * *
#        j = 2: * * *

# i = 1, j = 0: * * *
#               *

# i = 1, j = 1: * * *
#               * *

# i = 1, j = 2: * * *
#               * * *

# i = 2, j = 0: * * *
#               * * *
#               *

# i = 2, j = 1: * * *
#               * * *
#               * *

# i = 2, j = 2: * * *
#               * * *
#               * * *

