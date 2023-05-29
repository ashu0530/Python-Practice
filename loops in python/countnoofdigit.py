#I/P: x = 9235
#O/P: 4

n = int(input("Please enter the value: "))
if n > 0:
    result = n%10
print(result)

count=0
while n > 0:
    n = n//10
    count=count+1
print("Count of digits is ", count)