#I/P: x = "geeks", y="for"
#O/p: x = "for , y= "geeks"

#using temporary variable

x = "geeks"
y = "for"
temp = y #temp = "for"
y=x  #y="geeks"
x=temp #x=for

print(x)
print(y)

a=10
b=20
temp2=b
b=a
a=temp2
print(a)
print(b)


#Another method using comma assignment
i=100
j=200

i,j=j,i #one line expression to swap two number
print(i)
print(j)

m,n,o=500,"geeks",10.5   #here m = 500, n = "geeks" o = 10.5
print(m)
print(n)
print(o)          

m,n = m-5,n+"for"  #vm=500-5=495 , n= "geeks" appending by + operator "for" n = "geeksfor"
print(m)
print(n)


