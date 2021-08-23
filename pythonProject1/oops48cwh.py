class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email=f"{fname}{lname}@gmail.com"
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email not set"
        return f"{self.fname}.{self.lname}@gmail.com"
    @email.setter
    def email(self,string):
        print("setting now")
        names=string.split("@")
        self.fname=names[0].split(".")[0]
        self.lname=names[0].split(".")[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
emp1=Employee("Utkarsh","Saxena")
#print(emp1.email)
#print(type(emp1))
#print(type("this is string"))
#print(id("this is string"))
o="this is string"
#print(dir(o))
#print(dir(emp1))

import inspect
print(inspect.getmembers(emp1))