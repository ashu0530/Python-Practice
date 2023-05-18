#continue keyword skip the further execution or statement but it still in the loop
for i in range(1, 101):
    if i%3==0 or i%5==0:   #number remainder = 0 then skip
        continue  #skip the remaining statement

    print (i)
print("bye")

for i in range(1, 101):
    if i%3==0 and i%5==0:   #number remainder = 0 then skip
        continue  #skip the remaining statement

    print (i)
print("bye")