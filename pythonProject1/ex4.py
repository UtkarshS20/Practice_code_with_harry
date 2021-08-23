a=int(input("no. of rows"))
n=int(input("enter 0 or 1"))
b=bool(n)
if b==True:

    for i in range(1,a+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif b==False:
    for i in range(a,0,-1):
        for j in range(i+1,1,-1):
            print("*",end=" ")
        print()
