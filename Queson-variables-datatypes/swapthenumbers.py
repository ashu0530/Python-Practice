#swap  two numbers 
#input: a=1, b=2  
#output: 2,1

#first method with temp variable
first=1
second=2
temp=first
first=second
second=temp
print(first)
print(second)

#2nd method
a=1
b=2

a,b=b,a
print(a)
print(b)