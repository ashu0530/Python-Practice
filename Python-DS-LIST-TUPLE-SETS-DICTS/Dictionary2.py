d = {110:"xyx", 101:"abc", 105: "bcd", 104: "abc"}

d[101]="wxy" #change the value of 101 key
print(len(d))
print(d) #Value changed of 101

print(d.pop(105))
print(d) #105 key value removed and output show value of poped out key

del d[110]  #The deletes the key value pair
print (d)

d[108] = "cde"
print(d)
print(d.popitem()) #its remove the last inserted key value pair
print(d)