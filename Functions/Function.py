#Function - A set of instructions that can be re-use any number of times, Also we have to change something then we will change in one place

def fun():                      #Syntax keyword def is define to create variable here fun is like variables
    print("fun() called")

print("Before calling fun()")
fun()  #Call the function
fun() #2nd times called
print("After calling fun()")


def printDate(d,m,y):
    print(d,m,y, sep="-")

print("India became independent on")
printDate("15","08","1947") #pass this value to above variable d,m,y

#Function can return values also

def getDate(d,m,y):
    return d+"-"+m+"-"+y   
print("India became independent on")
d = getDate("15","08","1947")
print(d)

#Best practice to retun the value instead of printing because whatever you get the value you can do later computation or operation in code

def greet_Msg():
    print("Hi")
    print("Welcome to ashu python world")

def exit_Msg():
    print("Please visit again")
    print("Bye")

greet_Msg()
print("Hope you are enjoying")
exit_Msg()


#Application of Functions ( or Methods )
#1- Avoid Code Redundancy and Ease Maintenance
#2 - Make code modular - takeInput(), processData(), produceOutput()
#3 - Abstraction ( for example, in library functions, we do not have to worry about internal working )
#4 - Avoid Variable name Collisions. Two different functions can use same variable name



################################ How Function Work ###################################################

def fun2():
    print("Inside fun2()")

def fun1():
    print("Before fun2()")
    fun2()
    print("After fun2()")

#Main code
print("Before fun1()")
fun1()
print("After fun1()")


#How these things functional call internally maintained - Internally system maintain function call stack

#A Stack is container or collection that allows insertions, deletions from one end only. 

#Main code   
#       |-> Before fun1()
#       |-> fun1()
#       |        |-> Beforefun2()
#       |        |-> fun2()
#       |        |        |-> Inside fun2()
#       |        |->After fun2()
#       |-After fun1()

def fun():
    x = 5
    y = 10
    x = x+5
    print(x,y)

fun() #10,10
fun() #10,10