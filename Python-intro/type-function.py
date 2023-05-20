#Type function tell us data type of variable or value it is built in function

a = 10
print(type(a))

b = 10.5
print(type(b))

c = 2+4j
print(type(c))  #complex class type

d= True
print(type(d))

e=None
print(type(e)) #NoneType so much used in datastructure

f="ashu"
print(type(f))

g=[10,20,30]   #Array list, same as vector
print(type(g))

h=(10,20,30)
print(type(h))

i={10,20,30}
print(type(i)) #set is a collection of items where all the items are distinct, check union,intersection no any order of item. The order is not matters, internally using hashing to implement keys keys are distinct

j={10 : "ashu", 20 : "Hanumanji"}  #Dictionary key value pairs
print(type(j))