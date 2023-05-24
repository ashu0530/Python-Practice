#Bit wise operator mainly work on binary representation, Binary number system are 0 and 1
#Decimal to binary 18
#18/2 Q=9 R=0  ^
#9/2  Q=4 R=1  |
#4/2  Q=2 R=0  |
#2/2  Q=1 R=0  |
#1/2  Q=0 R=1  |
#Binary = 10010 of decimal 18


#Binary to Decimal of 10010
#0X2^0 + 1x2^1 + 0x2^2 + 0x2^3 + 1x2^4  = 0+2+16 = 18


print(bin(18)) #0b10010
print(bin(12)) #0b1100

print(int("0b10010",2))  #2 is base
print(int("0b1100",2))

#Bitwise & operator
x = 3    #011
y = 6    #110   
        #=010 = 2   

print(x&y)  #2   

#Bitwise OR operator

x = 3 #011
y = 6 #110
     #=111 = 7 


print(x | y) #7


#Bitwise XOR operator
#0 0 0
#0 1 1
#1 0 1
#1 1 0

x = 3 #011
y = 6 #110
     #=101
print(x^y) #5
