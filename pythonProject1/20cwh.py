#l=10    #global variable
#def function1(n):
    #l=5 #local
#    m=8 #local
#    global l
#    l=l+45
#    print(l,m)
#    print(n,"i have printed")
#function1("thats me")
#print(l)

def utk():
    x=20
    def vaibhav():
        global x
        x=99
    print("before calling function",x)
    vaibhav()
    print("after calling function",x)
utk()
print(x)