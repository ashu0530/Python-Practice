a = [10,20,30,40,50,60,70,80]

a.remove(20) # remove function is remove the given value from list, if an item is not present and if you call a remove on this its raise a value error
print(a) 

print(a.pop()) #Remove the last element from the list
print(a)

print(a.pop(2)) #provide index to pop function
print(a)

del a[1] #Delete is general purpose keyword remove the item index at 1
print(a)

del a[0:2]  #index at 0 and 1 it will remove
print(a)

b = [10,40,20,50]
print(max(b)) #maximum value in the list

print(min(b)) #minimum value in list

print(sum(b))  #sum of all element in the list

b.reverse() # reverse the list
print(b)

b.sort() #increasing order sorting
print(b)

c = ["abc", "def" , "gfg" , "def"]
print(max(c)) #maximum value in the list

print(min(c)) #minimum value in list



c.reverse() # reverse the list
print(c)

c.sort() #increasing order sorting #lexographic order
print(c)



