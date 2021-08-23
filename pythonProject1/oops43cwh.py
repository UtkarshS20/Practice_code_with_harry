class A:
    classvar1="I am a class variable in class A"
    def __init__(self):
        self.var1="i am inside class A's constructor"
        self.classvar1="instance variable in class A"
        self.special="khaas hoon main"
class B(A):
    classvar2="I am in class B"
    classvar1 = "I am in class B"
    def __init__(self):
        #super().__init__()
        self.var1="i am inside a class B's constructor"
        self.classvar1="instance variable in class B"
        super().__init__()
        print(super().classvar1)

a=A()
b=B()
print(b.special,b.var1,b.classvar1)