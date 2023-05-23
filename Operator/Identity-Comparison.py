

x = 10     
y = x
print(id(x))
print(id(y))
print (x is y)
print ( x is not y)

x1=10  #literal if you create another literal with same then python doesn't create any memory location so variable is point to same literal memory address
x2=10
y1=20   
y2=20
z1="ashu"
z2="ashu"

print(x1 is x2)
print(y1 is y2)
print(z1 is z2)

#Containers

l1= [10,20,30]
l2= [10,20,30]
print(l1 is l2) #False its true only in case of literals like num value, floating, strings

x1 = None
x2 = None
print(id(x1))
print(id(x2))
print (x1 is x2)