l1=["bhindi","aloo","chopstcks","chowmein"]
#i=1
#for a in l1:
#    if i%2 is not 0:
#        print(f"buy {a}")
#    i+=1
for index,item in enumerate(l1):
    if index%2==0:
        print(f"buy {item}")