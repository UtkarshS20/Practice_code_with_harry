import time
a=time.time()
print(a)
k=0
while(k<40):
    print("hi its utkarsh")
    time.sleep(2)
    k+=1
print("while loop ran in",time.time()-a)
a1=time.time()
for i in range (41):
    print("hi its utkarsh")
print("for loop ran in",time.time()-a1)
localtime=time.asctime(time.localtime(time.time()))
print(localtime)