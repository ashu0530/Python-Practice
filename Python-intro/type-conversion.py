# Type conversion in Python 
# For example - you have a data of tuple and you want convert the tuple data into list to change
# Two ways we can change

# 1. Implict type conversion
a=10 #int
b=1.5  #float
c = a+b
print(c) #no loss of data

d = True
e=a+d #adding int with boolean value this bool upgrade to integer
print(e)

d = False
e = a+d
print(e)


#Explict type conversion
s = "135"
#i = 10+s
#print(i) #error cannot add integer with string
i = 10+int(s)
f = float(s)
print(i)
print(f)


#program 2
s="geeks"
print(list(s))
print(tuple(s))
print(set(s)) #unordered and allowed distinct values

#program 3
l = ['a', 'b', 'c']
print(l)
print(str(l)) #same result
print(str(l)[0:4]) 

a = 10
b = 11
print(str(a) + str(b)) #+ operator when we do string concatenate both string output is 1011

c = 12.5
print(str(c))

#program 4

t = (10,20,30) #tuple immutable
print(list(t)) #convert to list

s = {10,20,30} #set might be unordered once the list conversion done get in ordered/
print(list(s)) #convert to list 

#program 5
#binary hexadeciman octal

a = 20
print(bin(a)) #0b binary 0 and 1 
print(hex(a)) #0x hexa 0 to         000 10100   0x14
print(oct(a)) #0o octa 0 to 7 binary = 10100 =        010 = 2power1= 2      100  = 2power2 = 4  ans = 24 = 0o24 

#program 6

a = "1001"
print(int(a,2)) #2 is 2nd parameter default is 10.  2power3 = 8 + 1 = 9
b="12"
print(int(b,8)) #12 --> 12  8power0*2 = 2  + 8power1*1 = 8  8+2=10
c="A1"
print(int(c,16)) #A=10  16power1=16*10 = 160   1*16power0 = 1 == 161

