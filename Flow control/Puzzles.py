#Even-odd in python
#find the winner 

n = int(input("Enter number of coins: "))
print("Winner is: ")
if n%2 == 0:
    print("Opponent")
else:
    print("You")

#odd coins you first move  then you taking extra coin
#even coins last who choose is winner