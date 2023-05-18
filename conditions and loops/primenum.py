for i in range ( 1, 101):    #This loop run from 1 to 101
    if i > 1:                 #A prime number is a whole number greater than 1.
        for j in range (2,i):  #Another loop which run from 2 to number of i means.  2 will go through 2,3,4..101 also for 3 will go through 2,3,4,...101
            if (i%j == 0 ):  #condition if i loop value and j loop value remainder is 0 means its even
                break  #break the condition jump out of loop
        else:     
            print(i)  #remaining part print