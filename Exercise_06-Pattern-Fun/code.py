#prg to print the following pattern
#1 1 1 1 1
#2 2 2 2 
#3 3 3 
#4 4
#5
n=1
rows=int(input("Enter number of rows: "))
for i in range(rows,0,-1):
    print((str(n)+" ")*i)
    n+=1