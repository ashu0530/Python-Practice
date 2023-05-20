# Set in python - Items can be mixed like can be string integer
#Distinct items - no same items is allowed
#unordered - ordered is not predefined any permutation you can get.
#No indexing - because there is no ordering

#Advantages of sets over list is
# 1- Union, Intersection,  Set Difference, etc are fast because set using hashing, when you store items using hashing you can quickly do search, insert, deletion items.


s1={10,20,30}
print(s1)

s2=set([20,30,40]) #set constructor 
print(s2)

s3={}
print(type(s3)) #type dictionary

s4=set() #constructor style to create empty set
print(type(s4))
print(s4) #set()


s = {10,20}
print(s)
s.add(30)  #add 30 in the set
print(s)

s.update([40,50]) #pass the list square backet
print(s)

s.update({60,70}, [80,90]) #multiple collection set and list
print(s)


