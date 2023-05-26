#for x in seq:     #seq can ve list, string, tuple,set, range these are iterables
#    statement1
#    statement2
#    statement3

l = [10,20,30,40]
for x in l:
    print(x)


s = "ashu"
for x in s:
    print(x) #a 
    print(x) #a

for x in range(5):
    print(x)

for x in range(20):
    if x%6 ==0:  #multiple check of 6 value range between 20
        print(x)

l = [10,20,30,40]
for i in range(len(l)):
    print(i, l[i])

