r = range(5)
print(type(r))
print(r)
l = list(r)
print(l)

#range(x): 0,1 ..... x-1
#range(x,y): x,x+1,,,,,,,y-1
#range(x,y,z): x, x+z, x+2z, x+3z ....


r = range(10,20) #10 to 19
l = list(r)
print(l)

r = range (-2,2)
l=list(r)
print(l)

r = range(10,20,2)  #10,12,14,16,18  x,x+z,x+2z
l = list(r)
print(l)

r = range(10,20,3)  
l = list(r)
print(l)

r = range(20,10,-2)  
l = list(r)
print(l)

r = range(20,10,-3)  
l = list(r)
print(l)