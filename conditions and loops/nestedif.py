x=4
r=x%2

if r==0:      #if this is true then nested if run
    print("Even")
    if x>5:
        print("greater than 5")
    else:
        print("not greater than 5")

else:
    print("Odd")

print("Bye")