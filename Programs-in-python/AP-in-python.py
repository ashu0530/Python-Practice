# A person gets 5000 salary on 1st august 2020. The salary increases by 2000 every month. Find the salary that the person is going to get
#on 1st august 2025

#Formula for nth term of Arthematic-progression
#Arthematic progression- A series which has same difference between consecutive elements is called AP
#5000,7000,9000,11000,....   ?
#1st aug2020,                1st aug 2025
#5years = 61 months #including both august

#nth term = a + (n - 1 ) x d  a = first term , d = common difference
#5000+(61-1)x200 = 125000 ans

#a, a+d, a+d+d, a+d+d+Dd, ........
#a+0d, a+1d, a+2d, a+3d ........  a + (n-1) x d

#I/P : a=5, d=2,n=5         |     a = 10, d = 10, n = 101
#o/p: 13                    |     1010

a = int(input("Enter a:"))
d = int(input("Enter d:"))
n = int(input("Enter n:"))

result = a+(n-1)*d
print(result)


