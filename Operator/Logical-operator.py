#And - Take two boolean expression both boolean value is true then output = true
# OR - Either one expression be true then output be true
# ex1  ex2  and   or 
#  T    T    T    T
#  T    F    F    T
#  F    T    F    T
#  F    F    F    F

#Not is unary operator
#T   F
#F   T

a = 10
b = 20
c = 30

print(a<b and b<c)
print(a<b or b>c)
print ( not a > b)

#Expression that are treated as False: 

s1 = ""
s2= s1 or "DefaultStr" #if s1 is available then assign or choose "any key word"
print(s2)

s1 = "abc"
s2= s1 or "DefaultStr" #if s1 is available then assign or choose "any key word"
print(s2)

x = 10
print(x or 20) #x is true
      
y= 0
print(y or 30) 

z= 40
print(z and 50)
