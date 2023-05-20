#List in python - 
#List store collections of items together it is an array where we can store collections of items 

a = [10,20,30,40,50]  #index 0,1,2,3,4         -5,-4,-3,-2,-1,
print(a)  
print(a[3]) #40
print(a[-1])  #50
print(a[-2]) #40     


b = [10,20,30,40,50]
b.append(30)  #The append the items in the last of list
print(b)

b.insert(1,15) #inserts the items at given index here index is 1 and value is 15 shift toward right side
print(b) 

print(15 in b ) # to check it is present or not Result is in boolean
print(16 in b)

print(b.count(30)) #tell us the occurence of a  value here two 

print(b.index(30)) #tell us index of first occurence first check by in function then use index

print(b.index(30,4,7)) #4 is start index  which is inclusive and 7 is end index is exclusive from index 4 to 6 it search

