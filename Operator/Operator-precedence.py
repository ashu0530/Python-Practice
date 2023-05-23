# + -          precedence low
# * / //    to 
# **     high

print(5+2*3)
print(5+3*4**2)

#Associativity of operator -  > When you have two  or more operator of same precedence and expression then we use associativity to decide the valuation order
# + -  left to right
# * / // left to right
# ** //Right to left  


print(5+4-3) 
print(2**2**-1)
print((2**2)**-1) #bracket evaluated first associativity not apply