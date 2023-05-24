#I/P : x = 234
#O/P : 4
#only work x>=0
a = int(input("Enter a number"))
ld = a%10   #% operator give remainder    234/10 = Q = 23 R = 4
print("Last digit is", ld)


#For negative number 
x = int(input("Enter a number"))
ld2 = abs(x)%10  #-121 = 121  #absolute number
print("Last digit is " , ld2)


#For negative number if absolute function is missing 
y = int(input("Enter a number"))
ld3 = y%10 
print("Last digit is " , ld3)

#-121%10 = ( 9-13*10)%10 = 9
#-49%10 = (1-5*10)%10 =1  
