#prg to print the following pattern
#1 1 1 1 1
#2 2 2 2 
#3 3 3 
#4 4
#5
i=0
n=1
for i in range(5,0,-1):
    print((str(n)+" ")*i)
    n+=1