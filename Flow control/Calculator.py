import sys
print("""Please select operation:
1.Add
2.Subtract  
3.Multiply""")  #Triple coated string accross multiple line

choice = int(input("Select operation from 1,2 or 3: "))
if choice not in (1,2,3):
    print("Invalid choice")
    sys.exit() #function is get out of the code present in sys module
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if choice == 1:
    result = a + b
elif choice == 2:
    result = a - b
else:
    result = a*b
print("Result is", result)