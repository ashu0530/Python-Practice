# Print tables of number from 1 to 10

for i in range(1, 1*10+1, 1):  # 1 to range is 11 and increment by 1
    print(i, end=" ")
print()

for i in range(2, 2*10+1, 2):  # 2 to range is 11 and increment by 2
    print(i, end=" ")
print()

for i in range(3, 3*10+1, 3):  # 3 to range is 11 and increment by 3
    print(i, end=" ")
print()

# its two lengthy, and if user want to give some 1 to n i don't know what n can be

# Nested loops inside loop


# i*10+1 = range
for i in range(1, 2):  # i = 1  ,                        i = 2
    for j in range(i, i*10+1, i):  # j=1,2,3,4,5,6,7,8,9,10, j = 2,4,6,8,10,12,14,16,18,20
        print(j, end=" ")
print()

for i in range(1, 3):  # 1 ,2 value so this loop run for i = 1 and i = 2
    j = 1
    while j < 3:  # for i = 1 this loop run 2 times
        print(i, j)
        j = j+1
    print("Ashu")
