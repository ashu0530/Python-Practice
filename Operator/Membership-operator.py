#String : Check for substring
#Dictionary : Check for Key

#List, Set, Tuple etc: Check for membership
#in not in

s="Ashutosh"
print("g" in s)
print("A" in s)

#Dictionary

d = {10:"abc", 20:"efg"}

print(10 in d)
print (15 in d)
print (10 not in d )

#List
l = [10,20,30,40]
print(30 in l)
print([20,30] in l) #20 and 30 is sublist but its not a member  of the list

#Not in opposite of in