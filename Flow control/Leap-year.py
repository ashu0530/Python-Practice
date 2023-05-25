#Two people are born in same year 1948. In 2020, one person celebrating 72th birthday, but other person celebrates 18th, how?
#Ans is  Person 2 is born in 29th february and person1 is born on any other day.
#29th feb doesn't appear every year, it appears some certain years which called leap year

#Rule 1: Multiple of 4, but not multiple of 100.
#Rule 2: Multiple of 400
#Note: years like 2100,2200,2300,2500 are not leap year

y = int(input("Enter year: "))
if (y%4 ==0 ) and (y%100 !=0):  #rule 1
    print("Yes leap year")
elif (y%400==0):       #rule2
    print("Yes leap year")
else:
    print("No leap year")