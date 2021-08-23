l=["harry","larry","carry","garry"]
'''for i in l:
    print(i)'''
l1=[["harry",1],["larry",2],["carry",3],["garry",4]]
for i,j in l1:
    print(i,"and no. is",j)
d=dict(l1)
print(d)
'''
for i,j in d:
    print(i,j)'''
for i,j in d.items():
    print(i,j)
for k in d:
    print(k)