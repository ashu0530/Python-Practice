#by default input() function everything as a string
'''
a = input()
print (type(a))
b = input()
c=a+b
print(c)
'''

#print as it string

''' #multi line comment
x = input("Enter 1st number")
d = int(x)  #convert x into integer and save to d variable
y = input("Enter 2nd number")
e = int(y)
z=d+e
print(z)
'''

'''
x = int(input("Enter 1st number\n"))
y = int(input("Enter 2nd number\n"))
z=x+y
print (z)
'''

#printing first character of string
ch=input("Enter a char")
print(ch[0])  #index value to fetch the first character

ch2=input("Enter a char")[0] #it will go through all character of user input but only assigned 1st index to ch variable
print(ch2)


#Pass the evaulate the expression using eval function
result = eval(input('Enter an expression'))
print(result)









