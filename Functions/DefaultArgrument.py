#Default values indicate that the function argument will take that value if no argument value is passed during the function call. 
#The default value is assigned by using the assignment(=) operator of the form keywordname=value.

def printDetails(id, name="NA", price="NA"):
    print(f"ID is {id}")
    print(f"Name is {name}")
    print(f"Price is {price}")

printDetails(101,"abc",100)
print()
printDetails(102)
print()
printDetails(103,"xyz")

def student(firstname, lastname ='Mark', standard ='Fifth'):
	print(firstname, lastname, 'studies in', standard, 'Standard')

# 1 positional argument
student('John')

# 3 positional arguments						
student('John', 'Gates', 'Seventh')	

# 2 positional arguments
student('John', 'Gates')				
student('John', 'Seventh')



#John Mark studies in Fifth Standard
#John Gates studies in Seventh Standard
#John Gates studies in Fifth Standard
#John Seventh studies in Fifth Standard