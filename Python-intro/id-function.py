# ID function - is the built in function which give us the unique identifier for every object

print(id(5)) 
a=10 
print(id(a))   
b=a
print(id(b))

# b and a refer to same object which is 10 so we have for both unique identifier, it is id of the object
#Every object have unique identifier

x=10
y=10
print(id(x))
print(id(y))

#literals are stored in same address location x and y just pointing to it

i="geeks"
j="geeks"

print(id(i))
print(id(j))



#is operatior is check identity of two operands are same or not! ans is boolean

m = 10
n = 10
print(m is n)

c = m
print(c is n)

c =20 #new object is created c is refers to 20 value which have different address
print ( c is b )