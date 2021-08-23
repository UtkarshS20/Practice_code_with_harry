l=[1,2,3,4,5,6,7,8,9,0,"asd","efe"]
'''
for i in l:
    if type(i)==int and i>6:
        print(i)'''
for i in l:
    if str(i).isnumeric() and i>6:
        print(i)