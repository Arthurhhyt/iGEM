for x in range(10001):
    for y in range(x):
        if y!=0 and y!=1 and x%y==0:
            break
        elif y==x-1:
            print (x)
		   
