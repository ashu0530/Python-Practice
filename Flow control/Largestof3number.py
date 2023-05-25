#I/P : a = 10, b = 15, c = 7
#O/P = 15

x = int(input("Enter 1st num: "))
y = int(input("Enter 2nd num: "))
z = int(input("Enter 3rd num: "))

if ( x >= y ) and (x >= z):
    print("1st is the largest", x)
elif (y >=x ) and (y >= z):
    print("2nd is largest", y)
else:
    print("3rd is the largest", z)

print(max(x,y,z))
