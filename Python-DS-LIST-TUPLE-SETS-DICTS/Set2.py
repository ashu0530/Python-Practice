s={10,30,20,40}
s.discard(30)
print(s) #removed the 30 from the set Discard function- if you provide an item in discard , which is not present in the set, then its not going to do anything
s.discard(50)

# discard function work silently, not raise an error



s.remove(20) #remove function raises and error if the value is not present in it
print(s)

#if you want to be more careful about the item, or if you want to remove those items, then you can use remove with membership test function
# example if an item is present in the set using in operator 
# x in set then only remove x otherwise don't remove x
# So if you want to remove check its better to check for memebership first to avoid those error raise.


s.clear() #once you call clear function, everything is been removed from the set
print(s) #set() output

s.add(50) #add item
print(s)

del s #clear set itself gone no existence of s now, its clear the whole object is removed
#print(s) # s is not defined same thing happen with also list.


s = {10,20,30,40}
print(len(s))

print(20 in s)
print(50 in s) #in operator is fast compare to list because set use hashing internally

s1 = {2,4,6,8}
s2 = {3,6,9}

print (s1 | s2) #union, common occurance on time,  all items display, doesn't modify anything
print (s1.union (s2))
print (s2.union (s1)) 


print (s1 & s2) #intersection , give common elements in set & symbol is intersection
print (s1.intersection(s2))
print (s2.intersection(s1))

print( s1 - s2 ) #difference element 
print(s1.difference(s2))
print(s2.difference(s1)) #9 3

print(s1 ^ s2) #symmetric difference operator in context of sets it will find out present are both set but not common element except 6
print(s1.symmetric_difference(s2))


s1 = {2,4,6,8}
s2 = {4,8}

print(s1.isdisjoint(s2)) #False no common element  in both set then return true else false

print(s1<=s2) #subset operator 
print(s1.issubset(s2)) # s1 have more element and s2 have less return false

print(s1<s2) #proper subset 
print(s1>=s2) #superset
print(s1 >s2) #proper superset





