#map- applies a function to a whole list
#numbers=["2","34","432"]
#numbers=list(map(int,numbers))
#for i in range(len(numbers)):
#    numbers[i]=int(numbers[i])
#numbers[2]=numbers[2]+1
#print(numbers[2])
#def sq(a):
#    return a*a
#num=[2,3,4,5,6,76,875,85,3]
#square=list(map(sq,num))
#square=list(map(lambda a:a*a ,num))
#print(square)


#def sq(a):
#    return a*a
#def cube(a):
#    return a*a*a
#func=[sq,cube]
#for i in range(5):
#    val=list(map(lambda x:x(i),func))
#    print(val)

#lst=[1,2,3,4,5,6,7,8,9]
#def isgreater_5(num):
#    return num>5        #returns true or false
#gr_than_5=list(filter(isgreater_5,lst))     #filter function filters for true return values
#print(gr_than_5)
from functools import reduce
list1=[1,2,3,4]
num=reduce(lambda x,y:x+y,list1)
#num=0
#for i in list1:
#    num=num+1
print(num)