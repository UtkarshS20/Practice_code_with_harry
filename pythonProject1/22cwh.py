#lambda or anonymous functions (one liner way to make functions)
#def minus(a,b):
#    return a-b
#minus=lambda a,b:a-b
#print(minus(9,4))

a=[[1,14],[5,6],[8,23]]
a.sort(key=lambda x:x[1])
print(a)