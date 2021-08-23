class A():
    def __init__(self,first,second):
        self.f=first
        self.s=second
    def __pow__(self, power, modulo=None):
        return self.f**self.s
    def concat(self):
        return self.f+self.s
a=A(3,4)
b=A("squence1"," sequence2")
print(a.__pow__(25))
print(b.concat())
