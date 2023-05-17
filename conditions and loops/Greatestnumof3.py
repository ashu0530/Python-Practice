x = int(input("Enter 1st num"))
y = int(input("Enter 2nd num"))
z = int(input("Enter 3rd num"))

if x>y:
    if x>z:
        print("x is greater number")
elif y>x:
    if y>z:
        print("y is greater number")
    else:
        print("z is the greatest")
