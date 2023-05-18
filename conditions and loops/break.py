
'''
x = int(input("How many candies you want"))

i = 1
while i<=x:
    print("Candy")
    i+=1
'''

available = 10  #number of candies present 

x = int(input("How many candies you want"))

i = 1
while i<=x:

    if i>available:
        print("Out of stock")
        break    #jump out of the loop
    
    print("Candy")
    i+=1

print("Bye")
