#decorators- enhance the functionality of function
#def funct1():
#    print("heya")
#func2=funct1
#del funct1
#func2()
#def functreturn(num):
#    if num==0:
#        return print
#    if num==1:
#        return sum
#a=functreturn(1)
#print(a)
#def executor(func):
#    func("this")
#executor(print)
#decorator
def dec1(funct1):
    def nowexec():
        print("executing now")
        funct1()
        print("executed")
    return nowexec
@dec1
def slang():
    print("karma is a bitch")
#slang=dec1(slang)
slang()