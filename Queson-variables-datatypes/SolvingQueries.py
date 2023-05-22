#Given a dictionary, and a list of queries(keys), you have to find and print the value of each query from the dictionary if present else it prints "None" 

dict = {1:"abc", 2:"cde", 3:"fgh"}
query=[2,3,4]

print (dict.get(2))
print (dict.get(3))
print (dict.get(4))