#Print all those number in a list that are not multiple of 5
#I/P: l=[10,16,17,18,15]
#O/P: 16,17,18,19

l= [10,16,17,18,19,15]
for x in l:      #traversing in the list
    if x%5==0:
        continue #continue doesn't execute the statement after continue it simple move to 2nd iteration
    print(x)

for x in l:     #same as above
    if x%5 !=0:
        print(x)

#Using continue is always optional you can replace sum if condition but when you have a long loop written and you have so many things 
# #happening inside the loop and you don't want to execute those many things for some corner condition.
# 
#Example - You want to print all the items in e-commerce site like item,price,quantity,location you have multiple statement inside the loop
# you will be traversing through every item in the list and for every item you will be printing all the things.
# And now in the list there are some items whose price are not available, so those items you don't want to process
# So you run a loop to every item in the list, multiple print statement so it will print all the details of the items
# But you have a if condition where price is not available then CONTINUE do not process all the remaining statement for this particular item

i = 0
while i<=5:
    if i ==3:   #when this condition is true 
        i= i+1
        continue
    print(i, i*i)    #0,0    #1,1 #2,4  #condtion true i ==3 not print anything skipped, #4, 16, 5,25
    i=i+1    

l = [10,16,17,18,9,15,21,13]
for x in l:                 
    if x % 5 == 0:    #10 skipped,15 skipped
        continue
    if x % 7 == 0:
        break   #21 is true we get out of whole loop 
    print(x)   #16,17,18,9
print("bye")  #16,17,18,9,"bye"