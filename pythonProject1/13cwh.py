a=8
b=39
c=sum((a,b)) #built in
print(c)
def function1(a,b):
    print("you in function1",a+b)
#function1(5,7)
#print(function1(5,7))
def function2(a,b):
    """this function calculates average of two numbers
    this doesnt work for 3 no."""
    average=(a+b)/2
    #print(average)
    return average
v=function2(10,20)
print(v)
print(function2.__doc__)