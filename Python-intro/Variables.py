#Variable is used to store data in the memory later we can access the data using variable name, you can do computational using this data or modify this data or you
#can apply some logic on this data

age = 38   
name = "Ashu"
weight = 58.5

print(age)  #accessing the data using variable name
print(name)
print(weight)


price = 100
tax = 18

total_Price=price+tax
print(tax)

############################################ How Variables work internally ##################################################
# -> When you create a variable and you stored a value in, then a memory shell is created which have a value 10 and x becomes a label/reference to this memory location

x=10
y="geek"
z=20
w=z  #w will become a one more reference to same location z
w=13 #new memory is created where 13 is stored now w left the reference to z now its pointing address of 13

print(x,y,z,w)

#Variable is just referencing to memory location they don't have any type information associated with them, variables can be assigned any type of data

is_valid = True #boolean
marks = 90 #integer
pi = 3.14 #float
city_name = "varanasi" #string or char

print(is_valid)
print(marks)
print(pi)
print(city_name)

h = None #special value in python
print (h)  