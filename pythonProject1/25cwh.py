#def function_name_print(a,b,c,d,e):
#    print(a,b,c,d,e)
def fargs(normal,*args,**kwargs): #not compulsory to write *args only can be written as *argsabc etc
    #print(type(args))
    print(normal)
    #print(args[0])
    for i in args:
        print(i)

    for j,k in kwargs.items():
        print(f"{j} is {k}")
#function_name_print("utk","vaibhav","bitta","goli","shivam")
lst =["utk","vaibhav","bitta","goli","shivam"]
normal="this is normal argument and the students are: "
kw={"utk":"monitor","vaibav":"backbencher","shivam":"failure","bitta":"cook"}
# normal the *args then **kwargs only (not to be changed)
#args and kwargs are optional
fargs(normal,*lst,**kw)