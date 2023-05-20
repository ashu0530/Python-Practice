#Tuples are similar like list, it is in ordered and indexed, immutable we cannot change the value add remove after created it cannot be changed, faster than list
#Tuples are faster than list, collection of items which is fixed example collection of weeks days sunday monday
#tuples can be male female
#Access levels user access level which is 0 to 5 in software lifecycle

t= (10,20,"geeks")
print(t)

t = ()
print(type(t))
print(t)  

t=(10) 
print(type(t)) #single value it is create a integer value
t=(10,)
print(type(t)) #tuple type


#also we can write tuple in this way
t=10
print(type(t)) #integer
t=10,
print(type(t)) #tuple

t = 10,20,30,40,50
print(type(t))

print(t[2]) #30
print(t[-1]) #10

print(t[1:3]) #20,30 
print(len(t)) #5
print(t.count(10))
print(t.index(20))
