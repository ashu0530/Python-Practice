#Dictionary is similar to sets in many ways using hashing internally and items are unordered.
#Collection of key value pairs where key must be distinct, values may be repeated

#Dictionary in python is similar to hashmap in java or unordered map in c++, associated arrays in php
#Real world examples is Dictionary app
# We basically lookup for value of corresponding to the given key, insert a key-value pair, remove, access also and search also via key
# store the emp data emp id is key and emp data is value
# Storing frequencies of items, voting app


d = {110:"xyx", 101:"abc", 105: "bcd", 104: "abc"}
print(d)

d = {} #empty dictionary
d["laptop"] = 40000 
d["mobile"] = 15000
d["earphone"] = 1000
print(d)

print(d["laptop"]) #accessing the value
#print(d["iphone"]) #key error we get in square bracket access method when key is not present

d = {110:"xyx", 101:"abc", 105: "bcd", 104: "abc"}
print(d.get(101)) #key to get function we get the value
print(d.get(125)) #not present key, output is None

print(d.get(125,"NA")) #print NA

if 125 in d:   #same like above 
    print(d[125])
else:
    print("NA")

